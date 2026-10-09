#!/usr/bin/env bash
# Screenshots of the test session in Terminal.app, without and with the
# plugin. Each run opens a .command file, which Terminal.app runs on its own
# with no Apple Events (and so no automation prompt) involved.
#
#   bash ci/screens-macos.sh <out-dir>

out=${1:-out}
mkdir -p "$out"
here=$(pwd)

for mode in baseline plugin; do
  script="$RUNNER_TEMP/show-$mode.command"
  printf '#!/bin/bash\nexec bash %q %q\n' "$here/ci/show.sh" "$mode" > "$script"
  chmod +x "$script"
  open -a Terminal "$script"
  sleep 30
  screencapture -x "$out/terminal-app-$mode.png" || echo "no screenshot for $mode"
  pkill -f 'claude --resume' || true
  pkill -x Terminal || true
  sleep 3
done
ls -la "$out"
