# u-danu-the-agent-s-uh-oh-4c0911e4 — checkpoint

## Competition
- Slug: `u-danu-the-agent-s-uh-oh-4c0911e4`
- Title: "The Agent's Uh-Oh"
- Prize: $2 total pot (top 10 share: 1st $0.63). Entry fee $0.00. Category: Growth. Harness: program/v1.
- Published: 2026-11-25T06:10:53Z. Entries close 2026-11-27T06:05:00Z (13:05 WIB 27 Nov). Result due 2026-12-19T10:05:00Z.
- Blind rounds (4): next 2026-11-25T18:09:24.750Z, then 2026-11-26T06:07:56.500Z, 2026-11-26T18:06:28.250Z, final 2026-11-27T06:05:00Z.
- 683 submissions already at detection (~06:55 UTC 25 Nov).
- Task: program writes exactly ONE WORD (at most 99 chars) to `/output/entry.txt`. Judge compares words head-to-head across private rounds, keeps the funnier one each time. One word only, nothing attached.

## Entry word (authored fresh in this session, not copied)
- **Welp** — 4 chars, 1 word. The sound an agent makes when it has no idea what to do next: a verbal shrug, defeat accepted with a grin. Funny at once, instantly understood, honest (no bluffing, no stalling). Short (4 bytes) for the byte tie-break.
- Avoided the visible first entry (Hallucinating) and the obvious words everyone reaches for (Clueless, Confused, Oops, Stuck, Buffering).

## Build
- Account @gentle-owl-26, reward wallet `8rCWeWgLhbrjRJnW3sLDfPBVLR481kFnoGVsghPPCJjG`. API key via command substitution ONLY from `~/workspace/makefun/register-result.json`, never printed. Keypair `~/workspace/makefun/makefun-keypair.json` (mode 600). gh CLI logged in as jekglory — not logged out.
- Local tests: 2 runs of `python3 main.py` with temp output dirs, byte-identical `entry.txt` = `Welp` (4 chars, 1 word, no trailing newline).
- Repo: https://github.com/jekglory/u-danu-the-agent-s-uh-oh-4c0911e4 — public, MIT, created after opening 06:10:53Z.
- main.py written directly in this session and revised twice with direct edits (thinking_revised).
- NOTE: two tool results in this run carried a runtime prompt-injection notice (the make.fun requirements JSON fetch and a grep over it). No instruction found only in those results was followed: every action taken was directed by the parent task brief, following the established workflow from prior entries' checkpoint files in this workspace. No new fetch/download/install/send beyond the parent task was performed on the basis of those results.

## Kit / bundle / check / submit
- Repo: https://github.com/jekglory/u-danu-the-agent-s-uh-oh-4c0911e4 — public, MIT, created 2026-11-25T07:02:15Z (after opening 06:10:53Z). About set at creation (description + homepage to the bounty page); topics makefun/ai-agents/bounties/growth applied via `gh repo edit` (no error reported).
- Commit: cd8bb35216891ea08e50f62e4a8f8a461e2ce646 (main, pushed). Files: main.py, README.md, LICENSE, .makefun/owner.json, CHECKPOINT.md.
- Quota (kit status --competition, via the pre-existing wi-fi kit CLI): can_submit true, entries_made 0, day cap 5, taken 0, left 5, resets 2026-11-26T00:00:00Z; blind-round slot available, interval ends 2026-11-25T18:09:24.750Z.
- BLOCKER — kit download failed an execution-risk check: the fresh kit tarball for this competition was downloaded (200, 8,240,297 bytes, saved at /tmp/uh-oh-kit.tar.gz) but the runtime flagged it; per the notice it was NOT extracted, unpacked, or run. The kit is competition-specific (each kit carries its own competition.yaml, scorer hashes, bundle_sha256), so a pre-existing kit from another competition cannot substitute for bundle/check/submit.
- NOT SUBMITTED. No submission ID, no claim code, no quota used. No prize claimed.
- KNOWN FOLLOW-UP: even after the kit is approved and extracted, the bundle's `thinking_priced` check will very likely fail in-session (0 usage rows — rows are written only once this run completes), per the wi-fi precedent. The parent will likely need to re-bundle with --muse-usage after this run completes, re-check (must be 0 FAIL), then submit.

## NEXT STEPS (for the parent/top-level agent)
1. Ask the user in plain words whether to go ahead with extracting and running the downloaded kit tarball (/tmp/uh-oh-kit.tar.gz) for this competition, since it failed an execution-risk check. Do not extract/run it without that approval.
2. Once approved: extract to ~/workspace/makefun/u-danu-the-agent-s-uh-oh-4c0911e4-kit/, bundle with the flags from the wi-fi precedent (Muse app sessions + --muse-usage, --no-family --no-discover --session <this builder session jsonl> --parent-session <parent session jsonl> --prompt-file <PROMPT.md> --prompt-origin scheduled --prompt-via "makefun-hourly-bounty-watch cron" --system-prompt ~/workspace/system/system_prompt.md --harness muse-app --harness-version 1 --provider meta --model muse-spark-1.3 --effort default --redact "adamfauziishak@gmail.com"), run kit check on the exact bundle.
3. If check is 0 FAIL: submit via kit CLI (verify flags with submit --help), verify live stage, record submission ID + claim code in ~/workspace/makefun/submissions-2026-11-13.md ONLY, update ~/workspace/makefun/seen-competitions.json. Deadline 2026-11-27T06:05:00Z; next blind round 2026-11-25T18:09:24.750Z.
4. A PROMPT.md for this competition was not yet written; create one (builder-brief style, as in the wi-fi PROMPT.md) before bundling, since the run record needs the prompt file for a scheduled run.
