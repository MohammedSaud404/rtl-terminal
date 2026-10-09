#!/usr/bin/env bash
# Screenshots of the test session in real Linux terminals on a virtual
# display: xterm (no bidi), mlterm (fribidi), Konsole and GNOME Terminal
# (their own bidi), each without and with the plugin.
#
#   bash ci/screens-linux.sh <out-dir>

out=${1:-out}
mkdir -p "$out"
export DISPLAY=:99 LANG=C.UTF-8 LC_ALL=C.UTF-8
Xvfb :99 -screen 0 1400x900x24 >/dev/null 2>&1 &
sleep 3
eval "$(dbus-launch --sh-syntax)"

shoot() {
  local name=$1
  shift
  "$@" >/dev/null 2>&1 &
  local pid=$!
  sleep 25
  import -window root "$out/$name.png" || echo "no screenshot for $name"
  pkill -f 'claude --resume' || true
  kill "$pid" 2>/dev/null || true
  for app in xterm mlterm konsole gnome-terminal-server; do
    pkill -x "$app" 2>/dev/null || true
  done
  sleep 3
}

for mode in baseline plugin; do
  shoot "xterm-$mode" xterm -fa 'Noto Sans Mono' -fs 11 -geometry 110x40+0+0 -e bash ci/show.sh "$mode"
  shoot "mlterm-$mode" mlterm --geometry 110x40+0+0 -e bash ci/show.sh "$mode"
  shoot "konsole-$mode" konsole --nofork -e bash ci/show.sh "$mode"
  shoot "gnome-terminal-$mode" gnome-terminal --geometry=110x40+0+0 -- bash ci/show.sh "$mode"
done
ls -la "$out"
