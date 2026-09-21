# Team Handbook Project — Handoff for Adapting to a Different Age Group

This document captures everything from the "U15 Select 26 Season" Team Handbook project so it can be adapted for a different age group in a fresh chat. Paste this file's content (or attach it) into the new chat, along with `team-handbook.html` and `team-meeting.html`, and say which age group / team it's for and what should change.

## What this project is

A living "Team Handbook" for Matt Cunha's Junior Railers U15 Select team, maintained in two parallel places that must be kept in sync:

1. A Claude Project doc (`claude/team-handbook.md`) — the markdown source of truth.
2. A password-gated live website page, published via GitHub Pages from the `mcunha-railers/jrhc-schedule-feeds` repo:
   - `docs/team-handbook.html` — the full handbook, browsable like a normal page.
   - `docs/team-meeting.html` — a "presenter mode" slide-deck version of the same content, for walking the team through it live in a meeting (title/divider slides, one topic per content slide, keyboard/click navigation, a jump-to-slide menu, fullscreen toggle).

Both HTML pages are gated behind the same password ("railers") as Matt's existing Drill Library page, and styled to match it (Junior Railers brand: navy/red/blue rink theme, Teko/Public Sans/IBM Plex Mono fonts, light+dark mode).

## Critical workflow constraint — read this first

**Claude has no terminal or git access on Matt's computer.** The only way to touch his local repo is the device bridge (`mcp__remote-devices__*` tools), which can read/write files directly but cannot run git commands. The standing workflow for every change is:

1. Edit the file (usually staged from the device into the cloud workspace, or edited via the bridge).
2. Write the finished file to the exact path in Matt's local clone: `C:\Users\mattj\jrhc-schedule-feeds\docs\<file>` (via `SendUserFile` to get a `file_uuid`, then `device_commit_files` with that `file_uuid` — NOT a raw output path).
3. Hand Matt the exact `git add` / `git commit` / `git push` commands to run himself in his own terminal.

**Claude must never claim to run git directly — it can't.** This is a saved preference in Matt's persistent memory and should carry over to any new team/age-group version of this workflow.

## The final U15 Select handbook content (current, as of this handoff)

Use this as the starting template — most of Part 1 (rules) and Part 2 (logistics) will likely need only tone/detail changes for a younger or older age group; Part 3 (systems) is U15-specific and will need to be substantially rewritten for a different level.

```markdown
# 15U Select — Team Handbook (2026-27 Season)

This team is 15-year-olds — freshmen and sophomores in high school. The expectations below treat them like young adults who are responsible for themselves, not kids who need things done for them.

---

## Part 1 — Team Rules & Expectations

### Communication

- All communication about hockey goes **directly between coaches and players** — not through parents. If a player has a question, an issue, needs to report they'll miss something, or needs anything else, the player reaches out to a coach themselves.
- Parents should not be contacting coaches on a player's behalf. Questions about the player's own hockey (ice time, why a decision was made, etc.) should come from the player, not the parent.
- **[ADD LATER]** — the specific channel players use to reach coaches directly (text, email, team app) and confirmation that coaches' contact info has been shared with players, not just parents.

### Staying Informed (Crossbar)

- Check Crossbar regularly. Schedule changes, game/jersey info, and team communications get posted there — it's each player's job to stay on top of it, not something a coach will separately remind you about.
- Practice plans are typically posted by **2:00 PM on practice days**. Review the plan before you get to the rink — have a general idea of what we're working on and come prepared, both mentally and physically.

### Attendance

- **We expect players to be at practice.** Missing practice can impact playing time in games.
- We understand practices will be missed sometimes — fall school sports, family commitments, and other real conflicts happen, and that's understood. But we expect you to prioritize this team. Every player is an important piece of our development and success.
- There's a difference between a legitimate need (a big test you have to study for) and poor time management (you knew about it and put it off until the last minute, and now need the time because of that). The first is understood. The second isn't — be better about that.
- Players are responsible for updating their own attendance in Crossbar — not a parent's job.
- **[ADD LATER]** — how far in advance absences need to be reported.

### Equipment & Uniforms

- Full equipment at every practice and game — this includes neck guards. No exceptions.
- Correct jerseys and correct socks for practices and games — know what we're wearing before you show up.
- Bring **both uniforms (home and away) to every game.** Captains and players are responsible for figuring out which jersey the team is wearing that day — communicate with the other team's coaches to confirm before warmups. Come prepared to each game — no one, including coaches, should be searching for spare jerseys on game day.

### Playing Time, Lineups & Goalies

- **Playing time is not even — it's earned.** Coaches play the players who give the team the best chance to win. That's based on commitment, how a player is performing, attitude, and everything else that goes into being a good teammate — not a rotation or a guarantee.
- **Alternates:** we carry 3 alternates — Lucey, Reissner, Nordman. They're called on to play when the full-time roster (3 lines, 6 D, and 2 G) isn't fully available for a game.
- **Goalies:** we want our goalies playing full games. We'll alternate goalies throughout the season and announce who's playing the upcoming weekend at Thursday's practice.
  - If we feel a mid-game goalie change could have a positive impact on the game or the team, that can happen. We'll try to prepare goalies for what to expect, but part of being a goalie — especially if you didn't start — is being ready to help your team the moment you're called on.

### Respect & Conduct

- You represent yourself, your team, the Junior Railers, and your family — at all times, everywhere: on the ice, on the bench, in the locker room, at school, and at home. Make the right choices.
- Be respectful to teammates, coaches, officials, opponents, and rink staff.
- Support each other — on the bench, in the room, and outside the rink.

### Locker Room Policy

There's no other sport where you spend as much time together, or have anything quite like the atmosphere of the locker room. It's part of what makes hockey what it is — it can be fun, it builds relationships, and it brings a team closer together. It can also be dangerous: skate blades are sharp, and it doesn't take much for horsing around to turn into a real injury. Nobody wants to be the reason a teammate's season ends because things got out of hand in the room. Be respectful of each other and the space, and enjoy it for what it is.

- No cell phones or other recording-capable devices used in the locker room.
- Only players, coaches, and approved team personnel in the locker room — no outside visitors.
- **Locker rooms must be left clean** — every time, every rink. *(Click-to-enlarge link on the published pages — shows a photo of what "not left clean" looks like.)*

### Unacceptable Behavior

The following are not acceptable from anyone on this team, at any team activity (practice, game, tournament, locker room, or team travel):

- Disrespect toward officials, coaches, teammates, or opponents — arguing calls, taunting, verbal abuse.
- Fighting, or any attempt to injure another player, outside what happens within the normal course of play.
- **Bullying, hazing, or excluding a teammate.**
- Discriminatory language or behavior of any kind.
- **Phones or recording devices used in the locker room.**
- Unsportsmanlike conduct that reflects poorly on the team.
- Ignoring coaching instructions or team rules.
- Showing up late or unprepared without communicating with a coach in advance.
- **Possession or use of alcohol, tobacco/vaping products, or drugs at any team event.**

### Discipline & Suspensions

A tiered approach. Coaches always retain discretion to escalate based on severity — this is a floor, not a rigid formula.

This isn't limited to team events. An issue at school or at home becomes an issue with this team too — how you carry yourself off the ice reflects on this team, and can result in consequences here.

**Minor offenses** (disrespectful remarks, arguing with an official, not following equipment/uniform rules, locker room disruption, no-show without any notice):
1. First time: warning from a coach, conversation with the player.
2. Second time: expect to sit out.

**Serious offenses** (fighting or instigating, abusive language/gestures, deliberate attempt to injure, hazing/bullying, unauthorized recording in the locker room):
- Minimum 1–2 game suspension, at the coaching staff's discretion.
- A repeat serious offense adds additional games or removal from the team.

**Zero-tolerance offenses** (physical violence beyond the play of the game, harassment or discrimination, alcohol/drug/vape possession or use at a team event, hazing that causes harm):
- Immediate removal from the team event (practice, game, or otherwise).
- Multi-game suspension up to removal from the team for the season, at the coaching staff's and club leadership's discretion.
- Handled per USA Hockey SafeSport policy where applicable.

---

## Part 2 — Logistics

### Before Games

- **Arrive no later than 45 minutes before game time.**
- **Off-ice warmup starts 40 minutes before game time — led by the captains.** It must be organized and planned — captains own this; if it isn't working, we'll provide a plan to execute. Everyone participates (goalies are the only exception, if they have their own routine).
- Bring both uniforms to every game. Captains/players confirm with the opposing team's coaches which jersey we're wearing and communicate that to the team before warmups.
- Be **fully dressed before the Zamboni is on the ice.** By 10 minutes before game time, give full attention as coaches talk through the game plan — focus areas, how we can win, expectations.

### After Games

- When coaches enter the locker room, freeze — stop getting undressed and be ready to actively listen.
- Be supportive of your teammates. Not everyone makes the perfect play every time during a game — there's no calling out teammates.
- Discuss the game with constructive criticism, and continue to support each other.
- Move on: be upset if we lost, but understand it and learn from it. Be excited about a win, but stay humble — there's always room for growth.

### Practice

- Practice plans are posted by 2:00 PM on practice days (see Staying Informed above). Come prepared, with a general understanding of the plan for the day.
- Always bring effort — practice at high speed and high intensity, and challenge each other.
- Be present, both physically and mentally. Ask questions — this is the time to learn.
- Practice will be fun at times, fast at times, and slow or repetitive at times as we work through systems — understand that, and embrace it.
- If a coach is explaining something to one player, everyone else should be listening too — we don't want to repeat the same explanation multiple times.
- Help set up and transition between drills — pucks, nets, and other equipment — as we move from one drill to the next.
- If we're the last team on the rink for the night, bring the puck bag up to the Coaches Room — door code 1944.
- Same equipment standard as games: full gear including neck guards, correct jerseys and socks.

---

## Part 3 — Hockey Systems & Strategy

These are the systems we're actually running with this team. Not everything is filled in yet — new pieces get added as we cover them at practice.

### Even Strength

#### Forecheck

Structure: **2-1-2**, tightening into something close to a **2-3** depending on the read.

- **F1** — aggressive on the puck carrier.
- **F2** — in support.
- **F3** — stays high.

#### Neutral Zone — Regroup / Offense

- At least 2 of our 3 forwards need to be moving — ideally all 3.
- Objective: collect the puck with speed — we have a better chance of transitioning successfully into the offensive zone.

#### Neutral Zone Forecheck

##### 1-2-2 (Triangle)
- Our three forwards form a triangle: one man pressures the puck; the other two sit at the bottom of the triangle, not chasing in line with the pressuring forward.
- Both defensemen push up as much as possible, closing gaps.
- As the puck moves D-to-D or through the neutral zone, maintain the triangle shape as much as possible.

#### Defensive Zone

Traditional coverage:

- One D always fronts the net — make the opposing player uncomfortable: stick on them, body on them, move them. Don't let them claim space.
- The other D goes to the puck when it's in the corner on their side.
- Wings avoid going below the hash marks/dots — except in an emergency.
- Centers support the puck at all times.
- Wings take good lines/angles to take away the shooting lane: when the opposing point/defenseman has the puck, take away the shot first, forcing the play back down the wall or away from the net.

### Special Teams

#### Penalty Kill — In Zone

Basic **box**.

- Passive until it's the right time to be aggressive.
- Keep the puck outside — force shots/plays from outside "the house."
- Puck comes into the house → get aggressive. Puck stays outside the house → stay passive.
- Be aggressive to win a loose or mishandled puck and clear it.
- Return to passive as soon as the opponent regains full control.

#### Penalty Kill — Forecheck

##### Right Side Overload — *(a drill in the Drill Library)*
- Alignment: a 1 and a 3, with the "1" slightly forward of the "3," offset to the right side.
- Goal: take away half the ice on the opponent's breakout, forcing them up one side.
- The strong-side player (lined up on the red line) gets aggressive support; the other two players drop back into coverage.
- Avoid giving up cutbacks — force the play up one side and keep it there.

#### Power Play — Breakout

- Three players come up the ice together; two swing through the neutral zone — timing first, speed second.
- Move up the ice as a unit.
- Try to fill four lanes as we enter the offensive zone.
- First priority: possess the puck into the zone.
- If we're met with pressure after crossing the red line and can't carry it in clean: chip and chase — not dump and chase. Put the puck to a spot with intention, where we expect to win the race to it, then regain possession and get into our zone offense.

#### Power Play — In Zone

Running a **1-3-1**.

- Settle in — don't force it. Move the puck to whoever's open, using the bumper as an outlet.
- Look to create offense from below the circles.
- When the quarterback or the shooter is loaded up with the puck, make sure to have a net-front presence with our low player(s).
- When the play is with the point/passer, drop the net-front guy below the goal line for a low play: low-to-bumper, or point-to-shooter-to-backdoor to the net-front/low guy.

### Faceoffs

#### Defensive Zone Faceoffs

##### Stack (base alignment)
- This is our default for every defensive-zone draw unless we call something else (like a three-across) — most of the time, we're running the stack.
- The wing who'd normally line up on the boards side instead lines up in the middle and comes through the faceoff.
- Coverage progression if we don't win clean, in order: (1) the dot/puck, (2) the shooter, (3) the defenseman on the boards side.
- Everyone else on the draw has an assigned man/position to cover — these assignments are not negotiable.

##### "Doubles" (not a separate play)
- Not really its own play — still our stack alignment, just with both defensemen moved to the front of the net to match a situation where the other team puts two forwards there.

##### "Whiteout" (win play — bench call)
- Currently the only true faceoff *play* we run out of the defensive zone.
- On a clean win, puck goes back to the corner to the defenseman.
- The net-front wing (not the stack guy) breaks immediately, straight up ice toward the left hash marks of the center circle.
- The D banks a hard, indirect pass off the far-side boards, aiming just below the blue line, timed to meet the breaking forward. Well-timed, it can spring a breakaway.
- This is a bench call, not a player call — and it carries real risk.
- The D in front of the net must still cover their man, and we never force the pass through the middle unless it's completely open.

#### Offensive Zone Faceoffs

- **Diablo** — C wins the draw and passes to RW, who passes back to D1 for a shot from the point; LW rolls to the front of the net for a screen; C trails in behind for the tip/rebound. *(Fully diagrammed with animation in the Rink Board tool.)*
- **Bender** — center sets up the shooter on the center's backhand side; wins the draw backhand back to the shooter, who shoots.
- **Double Supreme** — stack two wings in front of the net; center takes the shot off the draw. Want the center on his forehand at the dot if possible.
- **[ADD LATER]** — two more offensive-zone faceoff plays to add to the library (Coach to recall details).
```

The full text is also in the attached `team-handbook.html` (easier to read, live-styled). The Claude Project doc `claude/team-handbook.md` in the "U15 Select 26 Season" project has this canonical markdown version if you keep working from inside that same project.

## Technical implementation notes (for whoever builds the new age's page)

- **Design system**: CSS custom properties for the Junior Railers brand — `--rink-navy`, `--rink-navy-deep`, `--faceoff-red`/`--faceoff-red-ink`, `--crease-blue`, `--ice`, `--surface`, `--ink`, `--steel`/`--steel-soft`, `--line`, `--frost`, `--focus-ring`. Fonts: Teko (headings), Public Sans (body), IBM Plex Mono (labels/eyebrows). Light/dark mode via `@media (prefers-color-scheme: dark)` plus a `[data-theme]` override.
- **Password gate**: SHA-256 hash check against a hardcoded hash, `localStorage` persistence with a page-specific key (e.g. `jrhc-team-handbook-unlocked` vs `jrhc-team-presenter-unlocked`) so unlocking one page doesn't unlock the other.
- **Presenter deck architecture** (`team-meeting.html`): a single `SLIDES` JavaScript array, each entry `{ type: "title"|"divider"|"content"|"diagram", section, title, body: [...] }`. Body blocks support `{p}` (paragraph), `{ul, twoCol}` (bullet list, optionally two-column), `{ol}` (numbered list), `{h, note}` (sub-heading + small note line). A `buildSlideEl()` function renders each slide; keyboard nav (arrows/space/Home/End), a jump-to-slide menu (Esc), a progress bar, and a fullscreen toggle are all built in.
- **Diagram embed**: one slide embeds a trimmed, self-contained copy of a separate "Rink Board" drill-diagram tool (SVG + vanilla JS physics/animation) via a `data:text/html;base64,...` iframe `src` — this avoids cross-origin/CSP issues a live link to a hosted artifact would hit. It has its own fullscreen overlay button/modal so the diagram is never visually cut off.
- **Image lightbox pattern**: any bullet that should open a full-screen photo (used here for "Locker rooms must be left clean") is rendered as a `<button class="img-link" data-img="assets/<file>.jpg">...</button>`, and a single delegated click handler + a reusable overlay (`<div class="diagram-overlay">` markup, an `<img>` instead of an iframe) opens/closes it — X button, click-outside, or Esc all close it. Both HTML pages implement this independently since they don't share JS.
- **Images**: stored under `docs/assets/` in the repo (e.g. `docs/assets/locker-room-clean.jpg`), compressed to ~1600px wide JPEG before committing, since the pages are otherwise plain static HTML.

## Verification pattern used throughout

Every change to either HTML page was verified with a headless Playwright browser (Chromium at `/opt/pw-browsers/chromium`) before deploying: load the page, unlock the password gate programmatically, jump to the changed slide(s) via the jump-menu, screenshot, and visually confirm the wording/formatting — plus a check for JS console errors. This caught a few real bugs along the way (a CSS specificity issue hiding the jump menu, un-decoded HTML entities, a diagram that was visually cut off) before they reached the live site.

## Open items still outstanding on the U15 version (may or may not carry over)

- An image for the "Alternates" bullet (Playing Time, Lineups & Goalies) was requested but never actually attached — still pending.
- Two more offensive-zone faceoff plays to add to Part 3 (Coach to recall details) — U15-specific, likely not relevant to a different age's systems section.
- A couple of small Part 1 logistics gaps ([ADD LATER] tags): the specific channel for direct player-coach communication, and how far in advance absences need to be reported.

## Suggested next steps for the new chat

1. Decide whether the new age group's handbook lives in the same repo (as a new file, e.g. `docs/team-handbook-<age>.html`) or a separate project/repo entirely.
2. If continuing in the same Claude Project ("U15 Select 26 Season"), just open a new chat inside that same project — the four project docs (including this one) are automatically available there via the Projects tool, no re-uploading needed.
3. If this is a genuinely separate team/project, attach this handoff file plus `team-handbook.html` and `team-meeting.html` to the new chat (or a new Claude Project you create for that team) and describe what needs to change for the new age group (tone, specific ages, systems/plays taught at that level, any different rules).
