"""Renders a crafted Claude Code session in a pseudo-terminal and reports what
lands on its screen: whether Claude Code reorders RTL text itself on this
platform, and how the plugin's layout comes out there.

  python ci/render.py prepare          seed the config and the test session
  python ci/render.py run <out-dir>    capture with and without the plugin

Linux and macOS only (ptyprocess). `prepare` rewrites ~/.claude.json, so it
refuses to run outside CI.
"""
import json
import os
import re
import select
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SESSION_ID = '00000000-0000-4000-8000-00000000c1a1'
COLS, ROWS = 100, 50
SETTINGS = json.dumps({'tui': 'default'})

PROMPT = 'وليش )hello( (some bugs( ??'
REPLY = '\n'.join([
    'مرحبا بالعالم',
    '',
    '- AdMob بيعرض إعلانه (plugin) التجريبي.',
    '',
    'اسمها (plugin) والـ repo (عام) و Google (Ads) والإصدار 2.1.294 جاهز.',
    '',
    'قال «مرحبا [كتير]» و `/rtl` و ✅ و ❤ هون.',
])
CONTROLS = {'RLM': '\u200F', 'LRM': '\u200E', 'RLI': '\u2067', 'PDI': '\u2069'}
LOGICAL = 'مرحبا بالعالم'
VISUAL = 'ملاعلاب ابحرم'


def prepare():
    if os.environ.get('CI') != 'true':
        sys.exit('prepare rewrites ~/.claude.json: run it in CI only')
    cwd = os.path.realpath(ROOT)

    config_path = os.path.expanduser('~/.claude.json')
    config = {}
    if os.path.exists(config_path):
        with open(config_path, encoding='utf-8') as f:
            config = json.load(f)
    config.update({'hasCompletedOnboarding': True, 'theme': 'dark'})
    config.setdefault('projects', {}).setdefault(cwd, {})['hasTrustDialogAccepted'] = True
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f)

    project = re.sub(r'[^A-Za-z0-9]', '-', cwd)
    folder = os.path.expanduser(os.path.join('~/.claude/projects', project))
    os.makedirs(folder, exist_ok=True)
    base = {'isSidechain': False, 'userType': 'external', 'entrypoint': 'cli', 'cwd': cwd,
            'sessionId': SESSION_ID, 'version': '2.1.294', 'gitBranch': 'main'}
    user = {**base, 'parentUuid': None, 'type': 'user',
            'uuid': '00000000-0000-4000-8000-0000000000b1', 'timestamp': '2026-10-08T08:00:00.000Z',
            'message': {'role': 'user', 'content': [{'type': 'text', 'text': PROMPT}]}}
    reply = {**base, 'parentUuid': user['uuid'], 'type': 'assistant',
             'uuid': '00000000-0000-4000-8000-0000000000a1', 'timestamp': '2026-10-08T08:00:05.000Z',
             'message': {'model': 'claude-opus-5-5', 'id': 'msg_ci_rtl', 'type': 'message',
                         'role': 'assistant', 'content': [{'type': 'text', 'text': REPLY}],
                         'stop_reason': 'end_turn', 'stop_sequence': None,
                         'usage': {'input_tokens': 1, 'output_tokens': 1}}}
    with open(os.path.join(folder, SESSION_ID + '.jsonl'), 'w', encoding='utf-8') as f:
        for row in (user, reply):
            f.write(json.dumps(row, ensure_ascii=False) + '\n')
    print('prepared session', SESSION_ID, 'in', folder)


def capture(with_plugin, extra_env=None, seconds=45):
    import ptyprocess
    import pyte

    args = ['claude', '--resume', SESSION_ID, '--settings', SETTINGS]
    if with_plugin:
        args += ['--plugin-dir', ROOT]
    env = {**os.environ, 'TERM': 'xterm-256color', **(extra_env or {})}
    proc = ptyprocess.PtyProcessUnicode.spawn(args, dimensions=(ROWS, COLS), env=env, cwd=ROOT)
    screen = pyte.Screen(COLS, ROWS)
    stream = pyte.Stream(screen)
    raw = []
    status = 'timeout'
    settled_at = None
    deadline = time.time() + seconds
    while time.time() < deadline and proc.isalive():
        ready, _, _ = select.select([proc.fd], [], [], 0.5)
        if ready:
            try:
                data = proc.read(65536)
            except EOFError:
                break
            raw.append(data)
            stream.feed(data)
            settled_at = None
        text = '\n'.join(screen.display)
        if 'Select login method' in text or 'claude setup-token' in text:
            status = 'needs login'
            break
        if 'trust this folder' in text:
            proc.write('\x1b[B')
            time.sleep(0.3)
            proc.write('\r')
            continue
        if LOGICAL in text or VISUAL in text:
            settled_at = settled_at or time.time()
            if time.time() - settled_at > 3:
                status = 'drawn'
                break
    if proc.isalive():
        proc.terminate(force=True)
    return status, ''.join(raw), [line.rstrip() for line in screen.display]


def run(out):
    os.makedirs(out, exist_ok=True)
    summary = {'platform': sys.platform}
    runs = (
        ('baseline', False, None),
        ('plugin', True, None),
        # Claude Code reorders RTL itself in VS Code's terminal on Windows;
        # does it on this platform too?
        ('vscode-baseline', False, {'TERM_PROGRAM': 'vscode'}),
        ('vscode-plugin', True, {'TERM_PROGRAM': 'vscode'}),
    )
    for name, with_plugin, extra_env in runs:
        status, raw, lines = capture(with_plugin, extra_env)
        with open(os.path.join(out, f'{name}.raw.txt'), 'w', encoding='utf-8') as f:
            f.write(raw)
        with open(os.path.join(out, f'{name}.screen.txt'), 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        logical = any(LOGICAL in line for line in lines)
        visual = any(VISUAL in line for line in lines)
        summary[name] = {
            'status': status,
            # Where the reply's first line landed: in the order it was
            # written (the terminal is left to reorder it) or already
            # reordered by Claude Code.
            'order': 'visual' if visual and not logical else 'logical' if logical and not visual else 'unknown',
            'rtl_lines': [line for line in lines if re.search(r'[\u0590-\u08FF]', line)],
            # Which direction controls Claude Code passed on to the terminal.
            'controls': sorted(name for name, ch in CONTROLS.items() if ch in raw),
        }
        print(f'== {name}: {status}')
        print('\n'.join(line for line in lines if line.strip()))
    reorders = summary['baseline']['order']
    summary['claude_reorders_rtl'] = {'visual': True, 'logical': False}.get(reorders)
    summary['claude_reorders_rtl_in_vscode'] = {'visual': True, 'logical': False}.get(
        summary['vscode-baseline']['order'])
    with open(os.path.join(out, 'summary.json'), 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print('== summary')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    command = sys.argv[1] if len(sys.argv) > 1 else ''
    if command == 'prepare':
        prepare()
    elif command == 'run':
        prepare()
        run(sys.argv[2] if len(sys.argv) > 2 else 'out')
    else:
        sys.exit(__doc__)
