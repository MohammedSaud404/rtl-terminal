# Changelog

All notable changes to rtl-terminal are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [1.0.5] - 2026-10-10

### Fixed

- While the preview of an RTL draft shows, the band above the input box keeps what Claude Code and other plugins draw there, with the preview under it. Before, the preview took the band's place and hid other plugins' rows, such as usage or warnings. Reported by karanb192.

## [1.0.4] - 2026-10-09

### Changed

- The directory listing's documentation link opens the README's usage section. Linking the installation guide made the directory hold the plugin for review, because the guide links the README and the README shows screenshots.

## [1.0.3] - 2026-10-09

### Added

- Links for the plugin directory's listing in `plugin.json`: documentation (the installation guide), support (this repository's issues), privacy (the README's privacy section) and terms (the MIT license). Claude Code itself doesn't read them, so nothing changes in use.

## [1.0.2] - 2026-10-09

Fixes every finding of Anthropic's plugin directory validation.

### Added

- A listing icon for the plugin directory.
- A README section describing every event the plugin hooks and what it does there.

### Changed

- bidi-js is now its original ES module source, unmodified, in place of its bundled build. Unicode conformance is unchanged: 91,707 of 91,707.
- The plugin keeps its settings in its own store and redraws when they change, so `plugin.json` no longer needs a `types` field.

### Removed

- The cross-platform CI jobs that needed a Claude Code token, and the `ci/` scripts. `checks.yml` keeps the strict validation, the tests and the conformance test, and uses no secrets.

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

[1.0.5]: https://github.com/MohammedSaud404/rtl-terminal/releases/tag/rtl-terminal--v1.0.5
[1.0.4]: https://github.com/MohammedSaud404/rtl-terminal/releases/tag/rtl-terminal--v1.0.4
[1.0.3]: https://github.com/MohammedSaud404/rtl-terminal/releases/tag/rtl-terminal--v1.0.3
[1.0.2]: https://github.com/MohammedSaud404/rtl-terminal/releases/tag/rtl-terminal--v1.0.2
[1.0.1]: https://github.com/MohammedSaud404/rtl-terminal/releases/tag/rtl-terminal--v1.0.1
[1.0.0]: https://github.com/MohammedSaud404/rtl-terminal/releases/tag/rtl-terminal--v1.0.0
