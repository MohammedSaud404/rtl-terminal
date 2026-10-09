// Types for the parts of bidi-js 1.0.3 this plugin uses.

export type EmbeddingLevels = {
  levels: Uint8Array
  paragraphs: { start: number; end: number; level: number }[]
}

export type Bidi = {
  getEmbeddingLevels: (text: string, explicitDirection?: 'ltr' | 'rtl') => EmbeddingLevels
  getReorderSegments: (
    text: string,
    embeddingLevels: EmbeddingLevels,
    start?: number,
    end?: number,
  ) => [number, number][]
  // Takes the levels themselves, unlike getReorderSegments.
  getMirroredCharactersMap: (
    text: string,
    levels: Uint8Array,
    start?: number,
    end?: number,
  ) => Map<number, string>
}

export default function bidiFactory(): Bidi
