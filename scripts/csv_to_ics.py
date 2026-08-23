#!/usr/bin/env python3
"""
Convert an E9 (vahockey.com/Valley Associates) admin-portal games export
(CSV with columns GameNo,GameDate,StartTime,Duration,Location,HomeTeamName,
HomeTeamShortName,VisitingTeamName,VisitingTeamShortName) into one .ics
feed per Junior Railers team, filtered to games that team plays in.

Usage:
    python csv_to_ics.py <source.csv> <output_dir>

Writes one <slug>.ics per distinct Junior Railers team name found in the
CSV, and a manifest.json mapping team name -> filename, into <output_dir>.
Re-running with an updated CSV overwrites the same filenames, so published
URLs never change.
"""
import csv
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

EASTERN = ZoneInfo("America/New_York")
TEAM_PREFIX = "Junior Railers"


def slugify(name):
    slug = name.lower().replace(TEAM_PREFIX.lower(), "railers")
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    return slug


def parse_start(game_date, start_time):
    dt = datetime.strptime(f"{game_date} {start_time}", "%Y-%m-%d %I:%M %p")
    return dt.replace(tzinfo=EASTERN)


def fold(text):
    # RFC 5545 line folding: split at 75 octets, continuation lines start with a space.
    encoded = text.encode("utf-8")
    if len(encoded) <= 75:
        return text
    lines = []
    while len(encoded) > 75:
        cut = encoded[:75].decode("utf-8", errors="ignore")
        lines.append(cut)
        encoded = encoded[len(cut.encode("utf-8")):]
    lines.append(encoded.decode("utf-8", errors="ignore"))
    return "\r\n ".join(lines)


def escape_text(text):
    return text.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")


def build_event(row, perspective_team, perspective_short):
    start = parse_start(row["GameDate"], row["StartTime"])
    end = start + timedelta(minutes=int(row["Duration"]))
    start_utc = start.astimezone(timezone.utc)
    end_utc = end.astimezone(timezone.utc)

    is_home = row["HomeTeamName"] == perspective_team
    opponent_short = row["VisitingTeamShortName"] if is_home else row["HomeTeamShortName"]
    summary = f"{perspective_short} vs {opponent_short}" if is_home else f"{perspective_short} @ {opponent_short}"

    lines = [
        "BEGIN:VEVENT",
        fold(f"UID:e9-{row['GameNo']}@juniorrailers.com"),
        f"DTSTAMP:{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
        f"DTSTART:{start_utc.strftime('%Y%m%dT%H%M%SZ')}",
        f"DTEND:{end_utc.strftime('%Y%m%dT%H%M%SZ')}",
        fold(f"SUMMARY:{escape_text(summary)}"),
        fold(f"LOCATION:{escape_text(row['Location'])}"),
        "SEQUENCE:0",
        "END:VEVENT",
    ]
    return "\r\n".join(lines)


def build_calendar(team_name, events):
    header = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//Junior Railers//E9 Schedule Sync//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        fold(f"X-WR-CALNAME:{escape_text(team_name)} (E9)"),
    ]
    footer = ["END:VCALENDAR"]
    return "\r\n".join(header + events + footer) + "\r\n"


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    source_csv, output_dir = Path(sys.argv[1]), Path(sys.argv[2])
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(source_csv, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    teams = {}
    for row in rows:
        for name, short in (
            (row["HomeTeamName"], row["HomeTeamShortName"]),
            (row["VisitingTeamName"], row["VisitingTeamShortName"]),
        ):
            if name.startswith(TEAM_PREFIX):
                teams.setdefault(name, short)

    manifest = {}
    for team_name, short in sorted(teams.items()):
        team_rows = [
            r for r in rows
            if r["HomeTeamName"] == team_name or r["VisitingTeamName"] == team_name
        ]
        team_rows.sort(key=lambda r: (r["GameDate"], r["StartTime"]))
        events = [build_event(r, team_name, short) for r in team_rows]
        filename = f"{slugify(team_name)}.ics"
        (output_dir / filename).write_text(build_calendar(team_name, events), encoding="utf-8")
        manifest[team_name] = {"filename": filename, "game_count": len(events)}
        print(f"{team_name}: {len(events)} games -> {filename}")

    (output_dir / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
