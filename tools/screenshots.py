#!/usr/bin/env python3
"""Make the screenshot for the README and the AnkiWeb listing.

    python3 tools/screenshots.py [--plain] [--capture-wallpaper | --wallpaper PATH]

Writes docs/screenshot.png: Anki's main window with its title bar, labelled
"Before", beside the same window with AnkiBare, labelled "After": no title
bar, its space given to Anki's content, the rounded corners and shadow
kept. The labels are on the image, so they can't drift from the pictures.
Both in AnkiGlass (--plain for stock Anki), which AnkiBare pairs well with.

It's made with the add-ons' shared screenshot tools, in the kit's checkout
next to this one (../anki-addon-kit/screenshots/shots.py, or set
ANKI_ADDON_KIT), which describe how they look and what they need. The decks
are made up.
"""

from __future__ import annotations

import argparse
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
KIT = os.environ.get("ANKI_ADDON_KIT", os.path.join(os.path.dirname(ROOT), "anki-addon-kit"))
sys.path.insert(0, os.path.join(KIT, "screenshots"))
import shots  # noqa: E402

# Narrower than the kit's main window, so side by side they stay legible.
TITLED = (700, 560)
BARE = (TITLED[0], TITLED[1] + shots.TITLE_BAR)  # the same window, its title bar's space given to Anki
DECKS = shots.DECKS[:6]  # what fits the shorter window


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plain", action="store_true", help="stock Anki, without AnkiGlass")
    shots.add_wallpaper_args(ap)
    args = ap.parse_args()
    glass = None if args.plain else shots.load_glass()
    with shots.Session() as s:
        page = s.main_window("deck", shots.toolbar(glass), shots.deck_browser(glass, DECKS),
                             shots.deck_browser_bar(glass), glass)
        s.capture([{"url": page, "width": w, "height": h, "setup": "window.shotReady", "transparent": bool(glass),
                    "out": f"{name}.png"} for name, (w, h) in (("titled", TITLED), ("bare", BARE))])
        tint = glass and glass["tint"]
        out = s.side_by_side([
            {"image": "titled.png", "size": TITLED, "title": "User 1 - Anki", "tint": tint},
            {"image": "bare.png", "size": BARE, "title": "User 1 - Anki", "tint": tint, "bare": True},
        ], ["Before", "After"], shots.wallpaper_for(args, s), os.path.join(DOCS, "screenshot.png"))
    print("wrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
