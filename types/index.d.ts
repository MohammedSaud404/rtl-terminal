export type RtlIsEnabled = boolean
export type RtlIsPreviewOn = boolean
export type RtlDraft = string
/** Who reorders RTL rows here: Claude Code (the plugin lays them out) or the terminal. */
export type RtlReorderedBy = 'claude' | 'terminal'

declare module 'claude-code' {
  interface PluginState {
    'rtl-terminal': {
      isEnabled: RtlIsEnabled
      isPreviewOn: RtlIsPreviewOn
      draft: RtlDraft
      reorderedBy: RtlReorderedBy
    }
  }
}
