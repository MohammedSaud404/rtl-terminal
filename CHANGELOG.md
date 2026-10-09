# Changelog

All notable changes to rtl-terminal are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [1.0.1] - 2026-10-09

### Added

- A privacy and security section in the README: the plugin sends nothing, runs no commands, and stores only its own settings.
- `displayName`, `homepage`, `repository` and `keywords` in `plugin.json`, as Anthropic's plugin directory asks.

### Removed

- `.gitattributes`, whose line-ending rewrite the directory's validation refuses.

## [1.0.0] - 2026-10-09

The first release.

### Added

- Right-to-left layout for Claude Code replies in Arabic, Hebrew, Persian, Urdu and every other RTL script: right-aligned lines, bullets, numbers and quote bars on the right, and headings, bold, italics, code and links kept.
- Levels from the full Unicode Bidirectional Algorithm (bidi-js 1.0.3, which passes all 91,707 cases of Unicode 17's `BidiCharacterTest.txt`), with code spans and links isolated left-to-right.
- Brackets the right way round, including pairs typed backwards on RTL keyboard layouts.
- Character widths measured as Claude Code measures them, emoji sequences included, and text-style pictographs drawn two cells wide.
- The same layout for your own messages in the transcript.
- A live preview of an RTL draft above the input box (`/rtl input on|off`).
- `/rtl`, `/rtl on|off` and `/rtl mode auto|claude|terminal`, remembered across sessions.
- Automatic detection of where Claude Code reorders RTL text itself (Windows Terminal, conhost, VS Code's terminal); the plugin steps aside in other terminals.

[1.0.1]: https://github.com/MohammedSaud404/rtl-terminal/releases/tag/rtl-terminal--v1.0.1
[1.0.0]: https://github.com/MohammedSaud404/rtl-terminal/releases/tag/rtl-terminal--v1.0.0
