# jrhc-schedule-feeds

Public iCal (`.ics`) calendar feeds for Junior Railers Hockey Club team schedules, for leagues
that don't natively support calendar subscription (e.g. E9 / Elite 9, vahockey.com).

Each feed is a static `.ics` file under `docs/`, published via GitHub Pages, generated from a
manually-exported schedule (there's no public API for these league sites). See the
`e9-schedule-sync` tooling in this repo for the conversion script.

## Feeds

Regenerated from the E9 admin portal's games export (`GameNo,GameDate,StartTime,Duration,
Location,HomeTeamName,HomeTeamShortName,VisitingTeamName,VisitingTeamShortName`), filtered
per team. Paste the URL for a team into that team's Crossbar Games tab ("+Import").

| Team | League | Games | URL |
|------|--------|-------|-----|
| Junior Railers 13 - Elite | E9 | 28 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-13-elite.ics |
| Junior Railers 13 - Select 1 | E9 | 31 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-13-select-1.ics |
| Junior Railers 13 - Select 2 | E9 | 31 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-13-select-2.ics |
| Junior Railers 14 - Select 1 | E9 | 30 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-14-select-1.ics |
| Junior Railers 14 - Select 2 | E9 | 28 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-14-select-2.ics |
| Junior Railers 15 - Elite | E9 | 30 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-15-elite.ics |
| Junior Railers 15 - Select | E9 | 30 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-15-select.ics |
| Junior Railers 16 - Elite | E9 | 32 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-16-elite.ics |
| Junior Railers 16 - Select 1 | E9 | 30 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-16-select-1.ics |
| Junior Railers 16 - Select 2 | E9 | 30 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-16-select-2.ics |
| Junior Railers 17 - Elite | E9 | 30 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-17-elite.ics |
| Junior Railers 17 - Select 1 | E9 | 32 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-17-select-1.ics |
| Junior Railers 18 - Elite | E9 | 28 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-18-elite.ics |
| Junior Railers 18 - Select | E9 | 27 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-18-select.ics |
| Junior Railers 19 - Elite | E9 | 27 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-19-elite.ics |
| Junior Railers 19 - Select | E9 | 28 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-19-select.ics |
| Junior Railers U14F - Elite | E9 | 14 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-u14f-elite.ics |
| Junior Railers U14F - Select | E9 | 12 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-u14f-select.ics |
| Junior Railers U15 - Select | E9 | 11 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-u15-select.ics |
| Junior Railers U16 - Select | E9 | 12 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-u16-select.ics |
| Junior Railers U18 - Select | E9 | 12 | https://mcunha-railers.github.io/jrhc-schedule-feeds/railers-u18-select.ics |

## How it works

1. Someone with admin access to E9's admin portal exports the games CSV manually
   (no public API exists).
2. The export is dropped into a watched OneDrive folder
   (`Claude/E9 Schedule Sync/source/`).
3. `scripts/csv_to_ics.py` converts it into one `.ics` per Junior Railers team and commits
   the result into `docs/` (same filenames every run, so URLs never change).
4. GitHub Pages serves `docs/*.ics` at a stable public URL.
5. Each team's juniorrailers.com/Crossbar page imports its URL via "+Import" (Games tab),
   which re-syncs nightly.
