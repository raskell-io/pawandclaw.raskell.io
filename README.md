# paw-and-claw.raskell.io

Website for [Paw & Claw](https://github.com/raskell-io/paw-and-claw), a turn-based tactics game
of woodland armies. The site also hosts the playable web (WebAssembly) build at `/play/`.

**Live:** https://paw-and-claw.raskell.io

## Quick start

```bash
mise install          # tools
mise run serve        # site only, http://127.0.0.1:1111
mise run preview      # site + game, served like Cloudflare does (wrangler dev)
```

## Tasks

| Task | Description |
|------|-------------|
| `mise run serve` | Dev server with live reload (no game) |
| `mise run build` | Build the site into `public/` |
| `mise run fetch-game` | Put the latest web build of the game into `public/play/` |
| `mise run sync-game` | Refresh `data/` and `static/sprites/` from a `../paw-and-claw` checkout |
| `mise run preview` | Build, add the game, run `wrangler dev` |
| `mise run deploy` | Build, add the game, `wrangler deploy` |

## Structure

```
paw-and-claw.raskell.io/
├── config.toml           # Zola configuration
├── wrangler.jsonc        # Cloudflare Worker (static assets) + custom domain
├── content/              # Home, how to play, commanders, download
├── data/                 # factions, commanders, units (generated from the game's RON files)
├── sass/style.scss       # The game's palette: forest, parchment, gold; Alegreya type
├── scripts/
│   ├── fetch-game.sh     # Latest web build of the game -> public/play/
│   └── sync-game.py      # Game data, portraits, unit sprites, fonts -> data/, static/
├── static/               # Screenshots, sprites, fonts, icons, _headers
└── templates/            # Zola templates
```

## Hosting

The site is a Cloudflare Worker with static assets (`wrangler.jsonc`), on the custom domain
`paw-and-claw.raskell.io` in the raskell.io zone. `.github/workflows/deploy.yml` builds and
deploys on every push to `main`. It needs two repository secrets:

- `CLOUDFLARE_API_TOKEN`: a token with *Workers Scripts: Edit* (account) and
  *Workers Routes: Edit* (zone raskell.io)
- `CLOUDFLARE_ACCOUNT_ID`

Cloudflare serves at most **25 MiB per file**; `fetch-game.sh` fails the build if the game's
`.wasm` grows past that.

## Where the game comes from

`scripts/fetch-game.sh` takes the game's web build from, in order:

1. `PAW_WEB_DIR`, a local `tools/web/build.sh` output
2. the `web-latest` release of raskell-io/paw-and-claw (`paw-and-claw-web.tar.gz`)
3. the `github-pages` artifact of the game's latest successful *Web build* run

To redeploy the site whenever the game changes, the game's web workflow can send a
`game-updated` repository dispatch here (needs a token with access to this repo).

## Tech stack

- [Zola](https://www.getzola.org/): static site generator
- [mise](https://mise.jdx.dev/): tools and tasks
- [Cloudflare Workers](https://developers.cloudflare.com/workers/static-assets/): hosting
- [Alegreya](https://www.huertatipografica.com/en/fonts/alegreya-ht-pro): the game's typeface (OFL)

## License

MIT. Game art and data come from the [game repository](https://github.com/raskell-io/paw-and-claw).
