// What Claude Code's renderer draws for a laid-out row, with a full
// implementation of the Unicode Bidirectional Algorithm standing in for it.

import { LRM, RLM } from '../hooks/bidi'
import type { Span } from '../hooks/markdown'
import bidiFactory from '../hooks/vendor/bidi.mjs'

const bidi = bidiFactory()

// Claude Code's own on Windows terminals: reorders by the rules, base
// direction from the first strong character, mirrors nothing.
export function drawn(row: Span[]): string {
  const text = row.map(span => span.text).join('')
  const chars = text.split('')
  const embedding = bidi.getEmbeddingLevels(text)
  for (const [start, end] of bidi.getReorderSegments(text, embedding)) {
    chars.splice(start, end - start + 1, ...chars.slice(start, end + 1).reverse())
  }
  return chars.filter(ch => ch !== RLM && ch !== LRM).join('')
}

