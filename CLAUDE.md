# Notes for agents

AnkiBare is one of AIbrahimv2's Anki add-ons (AnkiWeb ID 1505882046): it
hides Anki's macOS title bar and window buttons while keeping the window's
rounded corners.

To release it, publish it, or edit its AnkiWeb listing, follow the
`anki-addon-release` skill. It covers all of the user's add-ons: the
changelog, building and checking the package, the GitHub release, AnkiWeb, the
listing and AnkiWeb search.

- **On the user's Mac** it loads by itself, from
  `~/.claude/skills/anki-addon-release`.
- **Anywhere else**, such as a cloud session, read it first:
  https://github.com/AIbrahimv2/AnkiStepwise/tree/main/.claude/skills/anki-addon-release
  (`SKILL.md`, and `scripts/` for the package and search checks).

This repo: `./build.sh` builds `dist/anki-bare.ankiaddon` from `src/`. On the
user's Mac, `src/` is symlinked into Anki's `addons21` folder as `anki-bare`,
and the AnkiWeb copy (`1505882046`) is turned off so only one runs.
