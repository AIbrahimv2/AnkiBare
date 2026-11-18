# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added

- **Liquid Glass with AnkiGlass.** On a Mac with AnkiGlass installed, the
  What's new and About window gets the same glass as Anki's main window.
  **Glass on add-on windows** in AnkiGlass's Settings turns it off.

### Changed

- **A wider What's new and About window**: each version's changes sit beside
  its number, and the other add-ons are laid out as cards.
- **The signature at the end of About signs itself**, stroke by stroke, as
  if written by hand when you scroll to it.
- Add-on emoji stand on their own now, without a box around them.
- About ends with links to AIbrahimv2's LinkedIn and Instagram, under the
  signature, and the signature opens AIbrahimv2's website.
- On a Mac, with Stepwise's, Skim's or AnkiGlass's window in front, ⌘,
  opens that add-on's settings instead of Anki's Preferences. Everywhere
  else it still opens Anki's.

## [1.1.0] - 2026-11-17

### Added

- The Config button in Tools → Add-ons opens What's new (this list of changes)
  and About (links, whether AnkiWeb has an update, and AIbrahimv2's other Anki
  add-ons, with an Install button).
- When any of AIbrahimv2's add-ons is updated, a card at the bottom of Anki's
  main window says so once, with a link to what's new.

### Changed

- Needs Anki 24.04 or newer, like AIbrahimv2's other add-ons.

## [1.0.0] - 2026-09-10

### Added

- Hides Anki's macOS title bar and its close, minimize and zoom buttons, and
  gives the space to Anki's content.
- The window keeps its rounded corners and shadow, and you can still drag it
  by its top edge and resize it from any edge.
- Close and minimize with ⌘W and ⌘M, or from the menu bar.

### Fixed

- The title bar stays hidden when the window is shown again, switches to or
  from full screen, or is laid out again.
