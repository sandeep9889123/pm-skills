# Use the updated repository and installed skills

Release 2.3.0 contains 105 skills across 13 plugins. pm-prototype-os has nine skills and five commands. Check the actual installed plugin version and skill names before assuming a new procedure loaded.

## Direct repository use

Read current main, or pull your local checkout using your normal Git workflow. In a connected LLM request the exact current skill path from sandeep9889123/pm-skills and ask it to identify the source revision. A fixed older commit or copied file keeps its old contents.

## Claude Code

Refresh the marketplace and update the installed plugin explicitly:

```bash
claude plugin marketplace update pm-skills
claude plugin update pm-prototype-os@pm-skills
claude plugin list
```

Repeat the plugin update for other installed pm-skills plugins whose revised procedures you use. Marketplace refresh alone is not a reliable substitute for updating an installed plugin. Use the installed scope if your version requires it. In a running session use `/reload-plugins` if Claude requests it; otherwise verify the version in a new session. For future updates, `/plugin` > Marketplaces > pm-skills > Enable auto-update is available in supporting Claude Code versions. Third-party marketplaces can have auto-update off by default. This repository does not change your account settings or silently install plugins.

## Claude chat and Cowork

Open Customize > Plugins, find the personal marketplace/plugin and use its available refresh/update controls, then inspect the installed version and the three new skill names. Interface and sync behavior vary by plan and version. A GitHub merge alone cannot establish that your cached account/session copy refreshed. Organization-managed marketplaces use the owner's configured sync/update flow; this public repository does not itself configure that flow.

If using a manually uploaded plugin or individual skill, replace the uploaded package with the updated files through the same upload flow. Include the selected skill's references folder. A manual upload has no automatic connection to future GitHub changes. Do not delete unrelated skills or local caches to force an update.

## Codex and other hosts

Refresh or update the repository-backed plugin using the host's supported plugin management, then verify the same skills directory and version. For copied skill folders, replace the complete selected folder. A native upload or copied snapshot requires a new upload/copy; repository changes do not rewrite an old attachment or chat.

## Verify what loaded

Check pm-prototype-os/.claude-plugin/plugin.json or .codex-plugin/plugin.json for version 2.3.0 and the actual presence of eval-annotation-guidance, eval-error-discovery and llm-judge-calibration. Ask for a task and inspect whether the relevant new procedure/reference was actually used. Presence and activation do not prove correctness; evaluate outputs against your product evidence.

Verified documentation, 2026-11-15: [Claude Code plugin management](https://code.claude.com/docs/en/discover-plugins) and [Claude plugin usage](https://support.claude.com/en/articles/13837440-use-plugins-in-claude). Recheck platform instructions when the UI or command behavior changes.
