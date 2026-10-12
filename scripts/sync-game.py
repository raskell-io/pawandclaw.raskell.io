#!/usr/bin/env python3
"""Copy art and data from the game repository into the website.

    scripts/sync-game.py [GAME_REPO]        # default: ../paw-and-claw

The game's RON files are the source of truth. This pulls what the site shows
(factions, commanders, units) into data/*.json for Zola's load_data, and copies
portraits, full-body commander figures, unit sprites and fonts into static/. Re-run it after the game's
roster or art changes, then commit the result.
"""
import json
import re
import shutil
import sys
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
GAME = Path(sys.argv[1] if len(sys.argv) > 1 else SITE.parent / "paw-and-claw").resolve()
DATA = GAME / "assets" / "data"
SPRITES = GAME / "assets" / "sprites"

FACTION_ORDER = ["western", "northern", "southern", "eastern", "nether"]


def entries(text, indent):
    """Split a RON map into (key, body) pairs by its `"key": (` lines."""
    pattern = re.compile(rf'^{" " * indent}"(\w+)": \(\s*$', re.M)
    marks = list(pattern.finditer(text))
    for i, mark in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        yield mark.group(1), text[mark.end():end]


def field(body, name):
    match = re.search(rf'\b{name}: "((?:[^"\\]|\\.)*)"', body)
    return match.group(1) if match else None


def power(body, name):
    match = re.search(rf"\b{name}: (?:Some\(\()?\(?\s*name: \"([^\"]+)\",\s*description: \"([^\"]+)\",\s*stars: (\d+)", body)
    if not match:
        return None
    return {"name": match.group(1), "description": match.group(2), "stars": int(match.group(3))}


def factions():
    text = (DATA / "factions.ron").read_text()
    out = {}
    for key, body in entries(text, 8):
        color = re.search(r"color: \(([\d.]+), ([\d.]+), ([\d.]+)\)", body)
        rgb = "#" + "".join(f"{round(float(c) * 255):02x}" for c in color.groups())
        animals = re.findall(r'"([^"]+)"', re.search(r"animals: \[([^\]]*)\]", body).group(1))
        out[key] = {"id": key, "name": field(body, "name"), "description": field(body, "description"),
                    "color": rgb, "animals": animals}
    return [out[key] for key in FACTION_ORDER]


def commanders():
    text = (DATA / "commanders.ron").read_text()
    out = []
    for key, body in entries(text, 8):
        out.append({
            "id": key,
            "name": field(body, "name"),
            "faction": re.search(r"faction: (\w+)", body).group(1).lower(),
            "personality": re.search(r"personality: (\w+)", body).group(1),
            "description": field(body, "description"),
            "figure": (SPRITES / "figures" / f"{key}.png").is_file(),
            "power": power(body, "power"),
            "super_power": power(body, "super_power"),
        })
    return out


def units():
    text = (DATA / "units.ron").read_text()
    out = []
    for key, body in entries(text, 8):
        cost = re.search(r"cost: (\d+)", body)
        out.append({"id": key, "name": field(body, "name"), "asset": field(body, "asset_name") or key,
                    "description": field(body, "description"), "cost": int(cost.group(1)) if cost else None})
    return out


def copy_tree(src, dst, pattern="*.png"):
    dst.mkdir(parents=True, exist_ok=True)
    for path in sorted(src.glob(pattern)):
        shutil.copy2(path, dst / path.name)


def fonts():
    """The game's Alegreya fonts, as woff2 when fontTools is around."""
    dst = SITE / "static" / "fonts"
    dst.mkdir(parents=True, exist_ok=True)
    for ttf in sorted((GAME / "assets" / "fonts").glob("*")):
        if ttf.suffix != ".ttf":
            shutil.copy2(ttf, dst / ttf.name)
            continue
        try:
            from fontTools.ttLib import TTFont
            font = TTFont(ttf)
            font.flavor = "woff2"
            font.save(dst / (ttf.stem + ".woff2"))
        except ImportError:
            shutil.copy2(ttf, dst / ttf.name)


def main():
    if not DATA.is_dir():
        sys.exit(f"no game data at {DATA}; pass the paw-and-claw checkout as the first argument")
    data = SITE / "data"
    data.mkdir(exist_ok=True)
    for name, value in [("factions", factions()), ("commanders", commanders()), ("units", units())]:
        (data / f"{name}.json").write_text(json.dumps({name: value}, indent=2, ensure_ascii=False) + "\n")
        print(f"data/{name}.json: {len(value)}")
    copy_tree(SPRITES / "portraits", SITE / "static" / "sprites" / "portraits")
    copy_tree(SPRITES / "figures", SITE / "static" / "sprites" / "figures")
    for faction in FACTION_ORDER:
        copy_tree(SPRITES / "units" / faction, SITE / "static" / "sprites" / "units" / faction)
    fonts()
    print("sprites and fonts copied")


if __name__ == "__main__":
    main()
