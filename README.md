# pawandclaw.raskell.io

Website for [Paw & Claw](https://github.com/raskell-io/paw-and-claw), a turn-based tactics game
of woodland armies. The site also hosts the playable web (WebAssembly) build at `/play/`.

**Live:** https://pawandclaw.raskell.io

## Quick start

```bash
mise install          # tools
mise run serve        # site only, http://127.0.0.1:1111
mise run preview      # site + game, served like Cloudflare Pages does
```

## Tasks

| Task | Description |
|------|-------------|
| `mise run serve` | Dev server with live reload (no game) |
| `mise run build` | Build the site into `public/` |
| `mise run fetch-game` | Put the latest web build of the game into `public/play/` |
| `mise run sync-game` | Refresh `data/` and `static/sprites/` from a `../paw-and-claw` checkout |
| `mise run preview` | Build, add the game, run `wrangler pages dev` |

## Structure

```
pawandclaw.raskell.io/
├── config.toml           # Zola configuration
├── content/              # Home, how to play, commanders, download
├── data/                 # factions, commanders, units (generated from the game's RON files)
├── sass/style.scss       # The game's palette: forest, parchment, gold; Alegreya type
├── scripts/
│   ├── cf-pages-build.sh # Cloudflare Pages build command
│   ├── fetch-game.sh     # Latest web build of the game -> public/play/
│   └── sync-game.py      # Game data, portraits, unit sprites, fonts -> data/, static/
├── static/               # Screenshots, sprites, fonts, icons, _headers
└── templates/            # Zola templates
```

## Hosting

Cloudflare Pages project `pawandclaw-raskell-io` (raskell.io account), connected to this
repository like the other Pages sites: every push to `main` deploys, pull requests get preview
URLs. Custom domain: `pawandclaw.raskell.io`.

- Build command: `scripts/cf-pages-build.sh` (installs Zola, builds, adds the game)
- Build output: `public`

Cloudflare Pages serves at most **25 MiB per file**; `fetch-game.sh` fails the build if the
game's `.wasm` grows past that.

## Where the game comes from

`scripts/fetch-game.sh` takes the game's web build from, in order:

1. `PAW_WEB_DIR`, a local `tools/web/build.sh` output
2. the `web-latest` release of raskell-io/paw-and-claw (`paw-and-claw-web.tar.gz`)
3. the `github-pages` artifact of the game's latest successful *Web build* run

Cloudflare's build machine has no GitHub login, so production builds rely on (2): the game's
*Web build* workflow uploads `paw-and-claw-web.tar.gz` to the `web-latest` release and then
calls this Pages project's deploy hook (`PAGES_DEPLOY_HOOK` secret in the game repo), so the
site redeploys with every new game build.

## Tech stack

- [Zola](https://www.getzola.org/): static site generator
- [mise](https://mise.jdx.dev/): tools and tasks
- [Cloudflare Pages](https://developers.cloudflare.com/pages/): hosting
- [Alegreya](https://www.huertatipografica.com/en/fonts/alegreya-ht-pro): the game's typeface (OFL)

## License

MIT. Game art and data come from the [game repository](https://github.com/raskell-io/paw-and-claw).
