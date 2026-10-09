# Installation guide

[العربية](INSTALL.ar.md) · [Back to the README](../README.md)

## Requirements

- **Claude Code 2.1.294 or later.** Check with `claude --version`, and update with `claude update`.
- **A terminal where Claude Code reorders right-to-left text itself**, for the full layout: Windows Terminal, conhost (the classic Command Prompt and PowerShell window), or VS Code's integrated terminal on Windows, macOS or Linux. In other terminals the plugin steps aside; see [Where it works](../README.md#where-it-works).

## Install from inside Claude Code

1. Run:

   ```
   /plugin install rtl-terminal --marketplace MohammedSaud404/rtl-terminal
   ```

2. Claude Code asks whether to add the marketplace `github:MohammedSaud404/rtl-terminal`. Answer `y`.
3. Pick a scope:
   - **User** (recommended): for you, in every project.
   - **Project**: recorded in the project's `.claude/settings.json`, to share with your team.
   - **Local**: for you, in this project only.
4. Claude Code confirms that rtl-terminal is installed and active. It works right away, and in every new session.

## Install from the command line

One command:

```
claude plugin install rtl-terminal --marketplace MohammedSaud404/rtl-terminal --scope user
```

Or in two steps:

```
claude plugin marketplace add MohammedSaud404/rtl-terminal
claude plugin install rtl-terminal@rtl-terminal --scope user
```

New sessions load the plugin on their own. A session that was already open picks it up after `/reload-plugins`.

## Check that it works

- Ask Claude anything in Arabic, Hebrew, Persian or Urdu. The reply should sit on the right, with bullets and numbers on the right.
- Run `/rtl mode`. In a supported terminal it answers that Claude Code reorders RTL rows here and the plugin lays them out.

## Update

```
claude plugin marketplace update rtl-terminal
claude plugin update rtl-terminal@rtl-terminal
```

Then restart Claude Code, or run `/reload-plugins`.

## Turn off or uninstall

To turn the layout off for a while, run `/rtl off`, and `/rtl on` to bring it back.

To remove the plugin:

```
claude plugin uninstall rtl-terminal@rtl-terminal
claude plugin marketplace remove rtl-terminal
```

## Troubleshooting

**Replies are still on the left.**
Run `/rtl mode`. If it says the terminal reorders RTL rows, you're in a terminal where the plugin steps aside on purpose; see [Where it works](../README.md#where-it-works). If you know Claude Code reorders text in your terminal, run `/rtl mode claude`. Also check that the layout is on with `/rtl on`.

**Nothing changed after installing.**
A session that was open during the install needs `/reload-plugins`, or a restart.

**The marketplace or the plugin isn't found.**
Check the spelling `MohammedSaud404/rtl-terminal`, then run `claude plugin marketplace update rtl-terminal`.

**Copied text comes out scrambled.**
Use Claude Code's `/copy` command: it copies a reply's original text, in reading order. A mouse selection copies the screen, where right-to-left text is held in display order.

**Something else looks wrong.**
[Open an issue](https://github.com/MohammedSaud404/rtl-terminal/issues) with a screenshot, your terminal's name, and the output of `claude --version`.
