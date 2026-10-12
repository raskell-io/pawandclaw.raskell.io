+++
title = "Download"
description = "Play in the browser, or run Paw & Claw on Windows, macOS and Linux."
template = "wiki-page.html"
+++

## Play in your browser

The quickest way in: **[play now](/play/)**. The browser version is the full game, compiled to
WebAssembly. It needs WebGL 2, which every current version of Safari, Chrome, Firefox and Edge
has. The first visit downloads about 30 MB; after that your browser keeps it cached.

## Desktop builds

Paw & Claw runs natively on **Windows**, **macOS** and **Linux**. Packaged desktop builds will
be published on the [GitHub releases page](https://github.com/raskell-io/paw-and-claw/releases)
as versions are tagged; until then, build it from source (below), which takes a few minutes.

The desktop version also loads **mods**: game data (units, terrain, commanders, damage tables)
lives in plain RON files that a `mods/` folder next to the game can override.

## Build from source

Paw & Claw is open source under the MIT license. With [Rust](https://rustup.rs) installed:

```sh
git clone https://github.com/raskell-io/paw-and-claw.git
cd paw-and-claw
cargo run --release
```

The web version builds with `tools/web/build.sh`; see the
[repository](https://github.com/raskell-io/paw-and-claw) for details.
