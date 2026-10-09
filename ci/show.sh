#!/usr/bin/env bash
# Runs inside a terminal window for a screenshot. First, probe lines showing
# what the terminal itself does with RTL text and the Unicode direction
# controls (each line starts with its probe, numbered at its end); then the
# test session in Claude Code, without the plugin (baseline) or with it.
#
#   bash ci/show.sh baseline|plugin

cd "$(dirname "$0")/.." || exit 1
# Terminals started by a desktop service do not inherit the job's
# environment (PATH, the token); the workflow leaves them here.
[ -f "$HOME/.rtl-ci.env" ] && . "$HOME/.rtl-ci.env"

# Direction controls as octal UTF-8, for the bash 3.2 of macOS.
RLM=$(printf '\342\200\217')
RLE=$(printf '\342\200\253')
PDF=$(printf '\342\200\254')
RLI=$(printf '\342\201\247')
PDI=$(printf '\342\201\251')

ar='مرحبا بالعالم (plugin) و (عام) 2.1.294'
en='AdMob بيعرض إعلانه (plugin) التجريبي.'
printf '%s\n' \
  "$ar — 1 plain" \
  "${RLM}$ar — 2 RLM" \
  "${RLI}$ar${PDI} — 3 RLI" \
  "${RLE}$ar${PDF} — 4 RLE" \
  "$en — 5 plain" \
  "${RLI}$en${PDI} — 6 RLI"
printf '\n'

args=(--resume 00000000-0000-4000-8000-00000000c1a1 --settings '{"tui":"default"}')
[ "$1" = plugin ] && args+=(--plugin-dir "$PWD")
exec claude "${args[@]}"
