#!/usr/bin/env bash
# Put the latest web (WebAssembly) build of the game into OUT_DIR.
#
#   scripts/fetch-game.sh [OUT_DIR]        # default: public/play
#
# Sources, in order:
#   1. PAW_WEB_DIR: a local build (tools/web/build.sh in the game repo)
#   2. the `web-latest` release of raskell-io/paw-and-claw (public, no token needed)
#   3. the github-pages artifact of the game's latest successful "Web build" run
#      (needs `gh` with a token that can read the game repo's Actions)
set -euo pipefail
OUT="${1:-public/play}"
REPO="raskell-io/paw-and-claw"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

rm -rf "$OUT"
mkdir -p "$OUT"

if [ -n "${PAW_WEB_DIR:-}" ]; then
    echo "Using local build in $PAW_WEB_DIR"
    cp -R "$PAW_WEB_DIR"/. "$OUT"/
elif curl -fsSL -o "$TMP/web.tar.gz" "https://github.com/$REPO/releases/download/web-latest/paw-and-claw-web.tar.gz"; then
    echo "Using the web-latest release"
    tar -xzf "$TMP/web.tar.gz" -C "$OUT"
else
    echo "No web-latest release; using the latest Web build run's artifact"
    run="$(gh run list -R "$REPO" --workflow "Web build" --branch main --status success --limit 1 --json databaseId -q '.[0].databaseId')"
    [ -n "$run" ] || { echo "no successful Web build run found" >&2; exit 1; }
    gh run download "$run" -R "$REPO" -n github-pages -D "$TMP"
    tar -xf "$TMP/artifact.tar" -C "$OUT"
fi

[ -f "$OUT/index.html" ] && [ -f "$OUT/paw_and_claw_bg.wasm" ] || { echo "game build is incomplete" >&2; exit 1; }

# Cloudflare serves at most 25 MiB per file
size=$(wc -c < "$OUT/paw_and_claw_bg.wasm")
if [ "$size" -gt 26214400 ]; then
    echo "paw_and_claw_bg.wasm is $size bytes, over Cloudflare's 25 MiB per-file limit" >&2
    exit 1
fi
echo "Game in $OUT (wasm $((size / 1024 / 1024)) MiB)"
