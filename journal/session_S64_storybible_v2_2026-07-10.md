# Session S64 — RoamWithChris Story Bible Protocol v2

**Date:** 2026-07-10
**Trigger:** Chris clarified RoamWithChris priority — mass-audience growth toward a full-time-viable channel is the PRIMARY goal; memoir-for-Auggie is the secondary frame carried inside the growth mechanics, not a separate track. Requested research into what other successful storytellers/channels do before changing the Bible.

## What changed

Updated `roamwithchris/RoamWithChris_StoryBible_Protocol.docx` from v1 to v2. All original sections preserved verbatim (Series Constants, Voice/POV, Characters, What/Where/When/Why, Beat list, Goals, Narrative Methods, The Lesson, Technical Requirements, Must Never Be Forgotten, Bible Approval). Six additions:

1. **Section 0 — Hook Engineering** (new, sits before Voice/POV). Forces a named hook category (Pattern Interrupt / Curiosity Gap / etc.) plus explicit text/audio/visual hook layers before any beat gets written.
2. **Cast Consistency Check** (added inside Section 2 — Characters). Confirms locked traits for recurring cast (Kate=planner, Golfii=warrior, Chris=narrator, Auggie=audience, Pumpkin=veteran) carry through every episode, and requires new characters get a role + a moment, not just a cameo.
3. **Section 4 — Stakes Ladder** (new). Separate from the beat list — names 3-5 rungs where tension visibly escalates, plus which beat resets attention at the midpoint.
4. **Expanded Goals section**: added DM-share trigger, completion promise, and series binge trigger alongside the existing save/comment/share triggers.
5. **Section 11 — Retention Review, Post-Publish** (new). Filled in after a reel goes live: hook rate, timestamp of steepest drop-off, likely cause, actual vs predicted triggers, one change to carry forward.
6. **Series Constants note**: added the ~1.7-second scroll-decision window and DM-shares as the highest-weight Reels algorithm signal (per 2026 platform data), to frame why Section 0 exists.

## Why (research summary)

Pulled from MrBeast's leaked production doc, current (2026) Reels algorithm guidance, and travel-vlog parasocial-relationship research:

- **Hook is non-negotiable and mechanical, not just creative.** 2026 data: ~45-50% of viewers drop in the first 3 seconds; the algorithm gates wider distribution on a 3-second hold rate. Reels are watched muted, so the on-screen text hook has to carry the point alone for a large share of viewers — hence forcing all three hook layers into the template.
- **DM shares, not just saves/comments, are the top Reels signal in 2026** — a hook that makes someone think "I'm sending this to ___" outperforms generic engagement hooks. Added as its own field rather than folding into "share trigger" because it's a different, more specific mental test to write toward.
- **Rising stakes ("dopamine ladder") is real and well-documented** — MrBeast's own $1→$1M→$1B yacht structure is the clearest public example. Added as its own section so pacing is planned deliberately rather than implicit in the beat list.
- **Recurring, consistently-traited characters build the parasocial bond that makes people return** — this shows up both in MrBeast's team notes ("same characters... build a parasocial relationship... a powerful reason to keep returning") and in academic travel-vlog research (parasocial interaction theory predicts repeat viewership and destination-intent). Auggie/Golfii/Kate/Pumpkin already function this way informally — the Bible now makes it a checked step.
- **Retention-graph review is the actual engine behind MrBeast's consistency** — his team fixes the exact timestamp where a video loses viewers on the next video rather than guessing. A solo channel can't get second-by-second graphs the same way, but can still log hook rate and eyeballed drop-off points after each post and feed it into the next Bible. Added as Section 11 to close the loop.

## What I deliberately did NOT change

- Did not touch Voice/POV, the signature opener/tagline, or the memoir framing — Chris confirmed growth is primary but didn't ask to drop the emotional core, and the two aren't in tension (concrete human stakes is what both good growth mechanics and good memoir storytelling actually require).
- Did not import "addiction loop" language from the Kallaway-style prompt Chris shared — same underlying mechanics (hook, escalation, payoff, next-loop bridge), but named and framed around measurable retention/growth behavior instead, which fits a family-facing brand better and is more directly actionable (a name like "hook rate" points to a metric you can check; "trigger" doesn't).
- Did not change anything about the already-locked Auggie Backpacking Reel Bible — that one is ready for script under the OLD template. Recommend re-running it through the new Section 0 (Hook) and Section 4 (Stakes Ladder) before scripting, since those are the two additions with the most leverage on performance. Flagging for Chris to confirm before I touch it.

## Open item for Chris

Auggie Backpacking Reel Bible was locked under v1. Want me to backfill Sections 0 and 4 for it now (10 min), or leave it as-is and apply v2 starting with the next story?

---

## v2.1 addendum (same session, later)

Ran a second-opinion critique pass on v2; Chris approved fixes; v2.1 pushed (commit 21439f6).

**Chris decision:** Signature opener moves AFTER the hook — "grabbing attention is priority." Opener is brand, not hook; new sequence: Auggie hero visual (frame-1 pattern interrupt) → AI baby text → first story beat lands → signature opener → story continues. Opener position stays a logged variable in Retention Review.

**Other v2.1 changes:**
1. Core/Extended split — Core (9 sections) required before script; Extended fills if time allows. Fixes the solo-operator risk of a bloated template getting skipped entirely.
2. Kill Criterion at top — "Would a stranger send this to someone? Name who and why in one sentence or park the story." Kills weak stories before edit costs.
3. Stakes Ladder reworded to Open-Question Ladder — each rung = what question the viewer holds and at which beat it resolves. Prevents duplicating the beat list.
4. Carry-forward field added to Bible Approval — next Bible must pull the previous episode's Retention Review change before approval. Closes the learning loop mechanically (never rely on memory).
5. Retention Review capped at 5 min, added "opener position tested" field.
6. Must Never Be Forgotten rule #7 added: opener never frame 1.

**Resolved conflict:** v2's Hook Engineering said open mid-action; series constant locked the opener sequence. v2.1 resolves: the Auggie visual IS the frame-1 hook and must carry motion/tension itself — stated explicitly in both the constant and Section 1.

---

## v2.2 addendum (same session)

Chris decisions: (a) hook subject varies per story — no Auggie default; series handshake ("Daddy tell me a story" + opener) lands at ~sec 4-6 after the hook, recognition after surprise. (b) Incorporate misdirection/mission-change mechanics. (c) Needs shot guides until ingrained. (d) Editing is the bottleneck — automate via Descript/Artie. (e) Shorts-first cross-posting now, long-form YouTube later — corrected to long-master-first-cut-shorts-from-it where footage supports. (f) No failure exit — reframed KPI to 20 reels shipped with completed Retention Reviews (reps-with-feedback, not followers). (g) Cover-first strategy adopted per MrBeast (cover concept now part of Kill Criterion).

**v2.2 pushed (commit 22e4451):** varied hook + fixed handshake constant; THE TURN section (false assumption / planted clues / reveal beat / hindsight check / mission change — never forced); beat list is now beats + shots + HAVE/NEED/AI/CUT footage status, script blocked until all resolve; Caption/Title block (caption first line = second hook, pinned comment = lesson, YT Shorts keyword title); cover concept + 0-3 word cover text in Kill Criterion; hook type/subject log in Retention Review; MNBF rules 8-10 added (never state the false assumption, never twist without clues, never repeat hook back-to-back).

**New companion docs:**
- `roamwithchris/RWC_Standing_Capture_Kit.md` (commit 420ecbf) — 10-item every-trip shot list + 48-hour voice-memo rule + format discipline.
- `roamwithchris/RWC_Production_Pipeline.md` (commit a4be4f7) — 8 steps capture→retention review with owner + tool per step; Descript silence-removal as primary edit accelerant; Artie owns beat-to-clip matching; cadence target 2-3/week; 20-rep commitment; long-form runway (master edit → cut shorts).

**Parked for dedicated sessions:** (1) Chris on-camera / personal brand strategy — prep discussion doc. (2) Auggie-at-scale pros/cons structured conversation with Golfii — prep discussion doc.

**Research basis for v2.2 additions:** twist craft (surprising-yet-inevitable, planted clues), South Park but/therefore rule, MrBeast cover-first + format-variety rules, 2026 platform data (first frame = auto-cover on feed + often YT Shorts thumbnail; grid crops 4:5/1:1 so cover text center-frame 0-3 words; YT Shorts search-indexed unlike TikTok; ~85% muted viewing; daily cadence > weekly excellence; completion rate > length).
