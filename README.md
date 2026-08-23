# jrhc-schedule-feeds

Public iCal (`.ics`) calendar feeds for Junior Railers Hockey Club team schedules, for leagues
that don't natively support calendar subscription (e.g. E9 / Elite 9, vahockey.com).

Each feed is a static `.ics` file under `docs/`, published via GitHub Pages, generated from a
manually-exported schedule (there's no public API for these league sites). See the
`e9-schedule-sync` tooling in this repo for the conversion script.

## Feeds

| Team | League | URL |
|------|--------|-----|
| _(to be added)_ | E9 | _(to be added)_ |

## How it works

1. Someone with admin access to the league site exports the schedule (Excel) manually.
2. The export is dropped into a watched folder.
3. A script converts it to `.ics` and commits the result into `docs/`.
4. GitHub Pages serves `docs/*.ics` at a stable public URL.
5. juniorrailers.com's Crossbar team page imports that URL via "+Import" (Games tab), which
   re-syncs nightly.
