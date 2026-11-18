#!/usr/bin/env python3
"""Make the screenshots for the README and the AnkiWeb listing.

    python3 tools/screenshots.py [--plain] [--capture-wallpaper | --wallpaper PATH]

Writes docs/before.png, Anki's main window with its title bar, and
docs/after.png, the same window with AnkiBare: no title bar, its space
given to Anki's content, the rounded corners and shadow kept. Both in
AnkiGlass (--plain for stock Anki), which AnkiBare pairs well with.

They're made with the add-ons' shared screenshot tools, in the kit's
checkout next to this one (../anki-addon-kit/screenshots/shots.py, or set
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


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--plain", action="store_true", help="stock Anki, without AnkiGlass")
    shots.add_wallpaper_args(ap)
    args = ap.parse_args()
    glass = None if args.plain else shots.load_glass()
    titled = shots.MAIN_SIZE
    bare = (titled[0], titled[1] + shots.TITLE_BAR)  # the same window, its title bar's space given to Anki
    with shots.Session() as s:
        page = s.main_window("deck", shots.toolbar(glass), shots.deck_browser(glass),
                             shots.deck_browser_bar(glass), glass)
        s.capture([{"url": page, "width": w, "height": h, "setup": "window.shotReady", "transparent": bool(glass),
                    "out": f"{name}.png"} for name, (w, h) in (("titled", titled), ("bare", bare))])
        tint = glass and glass["tint"]
        written = s.frames([
            {"image": "titled.png", "size": titled, "title": "User 1 - Anki", "tint": tint, "out": "before.png"},
            {"image": "bare.png", "size": bare, "title": "User 1 - Anki", "tint": tint, "bare": True,
             "out": "after.png"},
        ], shots.wallpaper_for(args, s), DOCS)
    for out in written:
        print("wrote", os.path.relpath(out, ROOT))


if __name__ == "__main__":
    main()
