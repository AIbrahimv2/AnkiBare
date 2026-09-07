# AnkiBare

A minimalist macOS add-on that hides Anki's window title bar for a clean, bare look.

The title bar is made transparent and its space is reclaimed by the content, and
the traffic-light buttons (close / minimize / zoom) are removed. The window stays
*titled* underneath, so macOS keeps its **rounded corners** and native shadow — it
just looks headerless.

## Behavior

- **No visible title bar or window buttons** — the header space is given back to
  Anki's content.
- **Rounded corners preserved** — because the window remains titled, macOS keeps
  rounding it (a fully borderless window would be square).
- **Dragging still works** — the (now invisible) title-bar strip along the top is
  still a drag handle, so you can reposition the window normally.
- **Resizing still works** — from the window edges and corners, as usual.
- Close / minimize with the usual shortcuts (⌘W, ⌘M) or the menu bar, since the
  buttons are gone.

Great on its own, and pairs cleanly with translucent-window add-ons (e.g.
AnkiGlass) since the rounded shape is kept.

## Requirements

macOS only. On Windows and Linux the add-on loads and does nothing.

## Before:

<img width="1800" height="1169" alt="image" src="https://github.com/user-attachments/assets/0d7ffa9a-0e8c-41f2-ae5a-b7e1c87a35ce" />

## After:

<img width="1800" height="1169" alt="image" src="https://github.com/user-attachments/assets/a2b75ee7-d4fc-4acb-8429-2a8f70220719" />
