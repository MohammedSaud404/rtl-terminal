// Checks the vendored bidi-js source against Unicode's own conformance test,
// BidiCharacterTest.txt: the resolved level of every character and the
// visual order of every line.
//
//   node scripts/conformance.mjs            # Unicode 17.0.0, downloaded
//   node scripts/conformance.mjs 13.0.0     # another version
//   node scripts/conformance.mjs ./BidiCharacterTest.txt

import { existsSync, readFileSync } from 'node:fs'

import * as bidi from '../hooks/vendor/bidi-js/index.js'

const arg = process.argv[2] ?? '17.0.0'
const source = existsSync(arg)
  ? readFileSync(arg, 'utf8')
  : await (await fetch(`https://www.unicode.org/Public/${arg}/ucd/BidiCharacterTest.txt`)).text()

let total = 0
let failed = 0
const failures = []
for (const line of source.split('\n')) {
  if (!line || line.startsWith('#')) continue
  const [codePoints, direction, , levelsField, orderField] = line.split(';')
  const text = String.fromCodePoint(...codePoints.trim().split(' ').map(hex => parseInt(hex, 16)))
  const expectedLevels = levelsField.trim().split(' ')
  total++

  const embedding = bidi.getEmbeddingLevels(text, ['ltr', 'rtl', undefined][Number(direction)])
  const unitOf = []
  for (let unit = 0, i = 0; i < text.length; i++) {
    unitOf.push(unit)
    unit += text.codePointAt(unit) > 0xffff ? 2 : 1
    if (unit >= text.length) break
  }
  const levels = unitOf.map(unit => embedding.levels[unit])
  const levelsOk = expectedLevels.every((level, i) => level === 'x' || Number(level) === levels[i])

  const order = [...levels.keys()]
  const pointOf = []
  unitOf.forEach((unit, point) => {
    pointOf[unit] = point
    pointOf[unit + 1] ??= point
  })
  for (const [start, end] of bidi.getReorderSegments(text, embedding)) {
    const a = pointOf[start]
    const b = pointOf[end]
    order.splice(a, b - a + 1, ...order.slice(a, b + 1).reverse())
  }
  const visual = order.filter(i => expectedLevels[i] !== 'x').join(' ')

  if (!levelsOk || visual !== orderField.trim()) {
    failed++
    if (failures.length < 5) failures.push(line.slice(0, 100))
  }
}

console.log(`BidiCharacterTest (${existsSync(arg) ? arg : `Unicode ${arg}`}): ${total - failed} of ${total} pass`)
for (const failure of failures) console.log(`  failed: ${failure}`)
process.exitCode = failed === 0 ? 0 : 1
