# Notes for agents

AnkiBare is one of AIbrahimv2's Anki add-ons (AnkiWeb ID 1505882046): it
hides Anki's macOS title bar and window buttons while keeping the window's
rounded corners.

To release it, publish it, or edit its AnkiWeb listing, follow the
`anki-addon-release` skill. It covers all of the user's add-ons: the
changelog, building and checking the package, the GitHub release, AnkiWeb, the
listing and AnkiWeb search.

- **On the user's Linux machine and Mac** it loads by itself, from
  `~/.claude/skills/anki-addon-release`.
- **Anywhere else**, such as a cloud session, read it first:
  https://github.com/AIbrahimv2/AnkiStepwise/tree/main/.claude/skills/anki-addon-release
  (`SKILL.md`, and `scripts/` for the package and search checks).

This repo: `./build.sh` builds `dist/anki-bare.ankiaddon` from `src/`. On the
user's Mac, `src/` is symlinked into Anki's `addons21` folder as `anki-bare`,
and the AnkiWeb copy (`1505882046`) is turned off so only one runs. It does
nothing on Linux: from the Linux machine, check it on the Mac (`ssh mac`).
The AnkiWeb listing (title, tags, versions, description) is in
`docs/ankiweb-listing.md`. Keep it matching what's live.

Anki's Config button for it opens the shared kit's window (What's new and
About). `src/kit/` is a copy of `../anki-addon-kit` (the
theme, the controls, the Settings / What's new / About dialog and the
notice after updates). Don't edit it here: change the kit and run its
`sync.py`; `build.sh` warns when it's behind. `build.sh` puts
`CHANGELOG.md` in the package, where What's new shows it to users, so
write it in their terms. Every change users will notice gets a line
under `## [Unreleased]` in the session that makes it: that's what the
next release is cut from. The release skill's `release_status.py` shows
what's waiting in every add-on.

## Screenshots

Make them on the Mac, always: `../anki-addon-kit/screenshots/on-mac.sh`
(with `tools/screenshots.py`'s arguments). They're shown on AnkiGlass's glass
and need macOS (Anki.app, Tahoe's wallpaper, Chromium.app, your collection).
On the Mac it runs `tools/screenshots.py`; from the Linux machine it runs it on
the Mac over SSH and copies the PNGs back into `docs/`. Don't run
`tools/screenshots.py` directly on Linux.
