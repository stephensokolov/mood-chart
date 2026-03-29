# Mood Chart PWA

## What this is
A daily mood tracking progressive web app (PWA) for bipolar disorder patients. Single-page app with no backend — all data is stored locally on the patient's device via localStorage.

## Live URL
https://stephensokolov.github.io/mood-chart/

## GitHub repo
git@github.com:stephensokolov/mood-chart.git

## Project structure
- `mood_chart.html` — The entire app (HTML, CSS, JS all in one file)
- `manifest.json` — PWA manifest (start_url is relative `"."` for GitHub Pages compatibility)
- `sw.js` — Service worker with network-first caching strategy
- `index.html` — Redirect to mood_chart.html (needed for GitHub Pages root URL)
- `icon-192.png` / `icon-512.png` — PWA icons

## Key architecture decisions
- **Single HTML file**: All code lives in `mood_chart.html` — no build step, no dependencies
- **No server/backend**: Zero data leaves the device. localStorage only.
- **GitHub Pages hosting**: Deployed from `main` branch, root folder
- **Network-first service worker**: Ensures updates are picked up immediately while still working offline
- **PWA Add to Home Screen**: Uses `apple-mobile-web-app-status-bar-style: default` to avoid notch overlap on iPhone

## How to deploy
Push to `main` branch — GitHub Pages auto-deploys within ~1 minute.

## Local project path
`~/Projects/mood-chart-app`

## How to run locally
A Python static server is configured in `.claude/launch.json`. Use `preview_start` with name "Python Static Server" or run:
```
python3 .claude/serve.py
```
Then open http://localhost:8080/mood_chart.html

## Important notes for modifications
- After changing `mood_chart.html`, bump the `CACHE` version string in `sw.js` so the service worker picks up changes
- The table uses sticky positioning for the first column (label cells) — any new rows in the table should include `position: sticky; left: 0; z-index` on their label cell
- Day number rows appear both at the top of the mood grid and repeated above the sleep row
- The manifest `start_url` must stay relative (`"."`) — an absolute path breaks GitHub Pages subdirectory hosting
