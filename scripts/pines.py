#!/usr/bin/env python3
"""Draw the hero's pine silhouettes as seamless, horizontally tiling SVGs.

    scripts/pines.py

The trees follow the game's title screen (`pine_layers` in src/ui/theme.rs):
three stacked triangles per tree, heights and spacing varied by a sine of the
tree's index, nearer rows larger and darker. Writes static/img/pines-*.svg.
"""
import math
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent
WIDTH = 1200

# name, tree height, colour, seed (the game's two title-screen rows)
LAYERS = [("far", 105.0, "#243426", 37.0), ("near", 140.0, "#172118", 71.0)]


def trees(tree_h, seed):
    """(x, height) for each tree across one tile, spaced like the game's rows."""
    spacing = tree_h * 0.55
    x, i, out = 0.0, 0.0, []
    while x < WIDTH:
        out.append((x, tree_h * (0.7 + 0.3 * (math.sin(i * 1.7 + seed) * 0.5 + 0.5))))
        x += spacing * (0.8 + 0.4 * (math.cos(i * 2.3 + seed) * 0.5 + 0.5))
        i += 1.0
    # Stretch the row so the last gap matches the first and the tile repeats cleanly
    scale = WIDTH / x
    return [(tx * scale, h) for tx, h in out]


def svg(tree_h, color, seed):
    height = round(tree_h * 1.05)
    base = height
    shapes = []
    for x, h in trees(tree_h, seed):
        w = h * 0.42
        for copy in (x - WIDTH, x, x + WIDTH):
            for tier in range(3):
                top = base - h + tier * h * 0.22
                half = w * (0.45 + tier * 0.25)
                bottom = base - h * 0.18 * (2 - tier)
                shapes.append(f"M{copy:.1f} {top:.1f}L{copy + half:.1f} {bottom:.1f}L{copy - half:.1f} {bottom:.1f}Z")
    path = "".join(shapes)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height}" width="{WIDTH}" height="{height}" '
            f'preserveAspectRatio="none"><path fill="{color}" d="{path}"/></svg>\n')


def main():
    out = SITE / "static" / "img"
    for name, tree_h, color, seed in LAYERS:
        (out / f"pines-{name}.svg").write_text(svg(tree_h, color, seed))
        print(f"static/img/pines-{name}.svg")


if __name__ == "__main__":
    main()
