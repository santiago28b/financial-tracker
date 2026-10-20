# Learner profile

Who I am as a learner, what I'm working on, and the drills that turn weaknesses
into strengths. Claude reads this at the start of every session and updates it
at the end. I can edit it too. It's mine.

**Goal:** a full-time backend role by 2027. Build projects on my own, without
blindly trusting AI.

**Background:** basic programming, Git, SQL, terminal, HTTP. No system design yet.
LeetCode practised separately.

---

## Weaknesses → drills

Each one has evidence (dated, from real sessions) so we can see the trend.

### 1. Starting from a blank file / not knowing how to begin
Drill: the **start-up ritual** (ROADMAP "How a session works", step 3) before
every build: 3 lines of plain English → signature → one failing test or expected
print. Solo reps (`S#.R`) test it without help.
Evidence:
- 2026-10-20 — self-reported.
- 2026-10-20 — S0.4: skipped the ritual and drew first; the ritual wasn't clear
  until it was shown with an example. Did it once that happened.
- 2026-10-20 — S1.1 (min): started docs/data-model.md from blank without help.

### 2. Giving up when stuck
Drill: write expected / actual / ruled out first, then the **hint ladder**
(L1 question → L2 concept + doc → L3 pseudocode). Log the highest rung each session.
Evidence:
- 2026-10-20 — self-reported.

### 3. Consistency
Drill: 30–45 min daily; a 10-minute **minimum session** counts on bad days.
Streak lives in ROADMAP "You are here".
Evidence:
- 2026-09-28 → 2026-10-20 — 3-week gap after S0.3 (classes).
- 2026-10-20 — back: S0.4 done in one sitting.
- 2026-10-20 — took a minimum session instead of skipping the day.

### 4. Including work I can't explain
Drill: before a session closes, explain any one line Claude picks. If I can't,
it gets rewritten or deleted.
Evidence:
- 2026-10-20 — S0.4: `docs/architecture.md` has a Mermaid block I couldn't
  explain. Delete it, or learn it, before the next session.
- 2026-10-20 — Mermaid block deleted; the plain-text diagram I wrote stays.

---

## Strengths

- 2026-09-28 — finished S0.1–S0.3 in one day; explains the request lifecycle
  (DNS → TCP → TLS → HTTP).
- 2026-10-20 — S0.4: got the login flow right after one question: the token
  travels React → Backend, and the Backend checks it.
- 2026-10-20 — S1.1 (min): reasoned that our table shouldn't store passwords
  because Supabase Auth keeps the hash.

---

## Hint ladder log

One line per session where a hint was used: `date — session — highest rung — what it was about`.

<!-- newest at the bottom -->

---

## Solo rep log

One entry per `S#.R`: `date — rep — finished? — where I got stuck — what I'd do differently`.

<!-- newest at the bottom -->
