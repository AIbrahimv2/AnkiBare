# Notes for agents

AnkiBare is one of AIbrahimv2's Anki add-ons (AnkiWeb ID 1505882046).

To release it, publish it, or edit its AnkiWeb listing, follow the
`anki-addon-release` skill. It covers all of the user's add-ons: the
changelog, building and checking the package, the GitHub release, AnkiWeb, the
listing and AnkiWeb search.

- **On the user's Mac** it loads by itself, from
  `~/.claude/skills/anki-addon-release`.
- **Anywhere else**, such as a cloud session, read it first:
  https://github.com/AIbrahimv2/AnkiStepwise/tree/main/.claude/skills/anki-addon-release
  (`SKILL.md`, and `scripts/` for the package and search checks).

This repo has no `src/` or `build.sh`. The add-on's files sit at the top, so a
package is a zip of `__init__.py` and `manifest.json`, without `meta.json`,
`README.md` or the git files.
