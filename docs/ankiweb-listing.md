# AnkiWeb listing

What's live at https://ankiweb.net/shared/info/1505882046. Edit it at
https://ankiweb.net/shared/upload?id=1505882046 (the `anki-addon-release`
skill has the steps), and update this file in the same session.

## Title

🐻 AnkiBare: remove Anki's macOS title bar for a clean, bare window

## Tags

hide title bar remove title bar titlebar hide traffic light buttons window buttons minimal minimalist clean modern bare ui borderless macos mac rounded corners tiling window manager yabai

## Search

Searched on 2026-11-15, before and after the tags above replaced the old
ones, with the `ankiweb_search.py` approach from the `anki-addon-release`
skill. "Results" is how many add-ons match now. AnkiWeb sorts results by
ratings, so an add-on without ratings comes after every rated match; the
words only decide whether it shows up.

- Tags match whole words. "study plan" didn't find the tag "study planner",
  while the title and description match parts of words ("mac" finds
  "macOS"). So the tags spell out the exact words people type.
- Neighbouring tags read as a phrase, so their order matters.
- Left out on purpose: "top bar", which was in the old tags: Anki's top bar
  is the Decks/Add/Browse toolbar, which AnkiBare doesn't hide. Also "zen",
  "distraction free", "full screen" and "header", which are other add-ons'
  jobs.

| Search | Results | Before | After |
| --- | --- | --- | --- |
| title bar | 10 | #6 | #6 |
| titlebar | 5 | absent | #5 |
| hide title bar | 2 | absent | #2 |
| remove title bar | 1 | absent | #1 |
| traffic light | 2 | absent | #1 |
| window buttons | 3 | not run | #3 |
| borderless | 3 | absent | #3 |
| rounded corners | 8 | absent | #4 |
| minimal | 115 | #68 | #62 |
| minimalist | 39 | #21 | #17 |
| clean | 361 | #180 | #179 |
| modern | 168 | #81 | #75 |
| macos | 371 | #142 | #168 |
| tiling | 26 | #17 | #17 |
| window manager | 4 | #2 | #2 |
| aerospace | 1 | #1 | #1 |
| yabai | 1 | not run | #1 |

## Support page

https://github.com/AIbrahimv2/AnkiBare

## Supported Anki versions

2.1.1 to 2.1.1 with no `-`, the form's default, so every version gets it.

## Description

Paste as is. AnkiWeb takes Markdown and basic HTML.

```markdown
# AnkiBare
A minimalist macOS add-on that removes the window title bar from Anki.

⚠️ Note on Window Movement

This add-on removes the title bar, which acts as the primary "handle" for clicking and dragging windows in macOS.

- The Dragging Limitation: Once the title bar is hidden, you will no longer be able to click and drag the window to reposition it.

- Resizing is preserved: You can still resize the window by clicking and dragging the edges or corners, but repositioning the window becomes significantly more cumbersome without the title bar.

- **Recommended Workflow: This add-on is intended for users who utilize a Tiling Window Manager (I use AeroSpace) to handle window placement automatically.**

## Before:

<img alt="image" src="https://github.com/user-attachments/assets/0d7ffa9a-0e8c-41f2-ae5a-b7e1c87a35ce" />

## After:

<img alt="image" src="https://github.com/user-attachments/assets/a2b75ee7-d4fc-4acb-8429-2a8f70220719" />
```
