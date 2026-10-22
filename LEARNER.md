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
- 2026-10-20 — S1.1: first ritual attempt was one generic line; needed 3 rounds of
  questions to get the entity shape down before writing fields.
- 2026-10-21 — S1.2: ritual again started as one generic line; got to 3 lines
  with 2 questions. Copied Claude's example for step 3, then wrote a real one
  (Category ↔ Transaction) when asked.
- 2026-10-21 — S1.3: ritual started with only step 3, but it was a real expected
  output. Added the Decimal check and the 3 English lines when asked, with no
  example to copy. Both predictions matched the shell.
- 2026-10-22 — S1.4: gave all 3 ritual lines in one go (first time), but line 1
  named a solution (a flag) instead of a requirement. Chose text over a sketch.

### 2. Giving up when stuck
Drill: write expected / actual / ruled out first, then the **hint ladder**
(L1 question → L2 concept + doc → L3 pseudocode). Log the highest rung each session.
Evidence:
- 2026-10-20 — self-reported.
- 2026-10-21 — S1.2: said "idk" / "not sure what you mean" twice but kept going
  after the next hint each time; didn't write expected / actual / ruled out first.
- 2026-10-21 — S1.3: didn't get stuck; no hints needed.
- 2026-10-22 — S1.4: didn't get stuck. Pushed back on the CSV trade-off ("we're
  not doing that") until shown it's in PLAN.md and S9.9.

### 3. Consistency
Drill: 30–45 min daily; a 10-minute **minimum session** counts on bad days.
Streak lives in ROADMAP "You are here".
Evidence:
- 2026-09-28 → 2026-10-20 — 3-week gap after S0.3 (classes).
- 2026-10-20 — back: S0.4 done in one sitting.
- 2026-10-20 — took a minimum session instead of skipping the day.
- 2026-10-20 — then turned it into a full 45-min S1.1.

### 4. Including work I can't explain
Drill: before a session closes, explain any one line Claude picks. If I can't,
it gets rewritten or deleted.
Evidence:
- 2026-10-20 — S0.4: `docs/architecture.md` has a Mermaid block I couldn't
  explain. Delete it, or learn it, before the next session.
- 2026-10-20 — Mermaid block deleted; the plain-text diagram I wrote stays.
- 2026-10-20 — S1.1: pasted Claude's sentence into data-model.md, then explained
  it in own words ("it already reaches the user through account_id"). Had
  Claude write DECISIONS 007 and 011 from my answers; re-read them.
- 2026-10-21 — S1.2: explained `Ref: users.id < accounts.user_id` correctly.
  erd.dbml has comments I didn't write in session; next time, check that I can
  explain them too.
- 2026-10-21 — S1.3: asked Claude to write DECISIONS 001/005 ("you know I get
  it"). Instead dictated the decision + why in own words; Claude pasted them verbatim.
- 2026-10-22 — S1.4: said 002 was saved when it was empty, then asked Claude to
  write it. Dictated instead, pasted verbatim. 004's Why ("i dont think we will
  double putting stuff") is thin; it doesn't name the CSV trade-off.

---

## Strengths

- 2026-09-28 — finished S0.1–S0.3 in one day; explains the request lifecycle
  (DNS → TCP → TLS → HTTP).
- 2026-10-20 — S0.4: got the login flow right after one question: the token
  travels React → Backend, and the Backend checks it.
- 2026-10-20 — S1.1 (min): reasoned that our table shouldn't store passwords
  because Supabase Auth keeps the hash.
- 2026-10-20 — S1.1: came up with the opening-balance Transaction on my own;
  spotted that a stored balance is redundancy.
- 2026-10-21 — S1.2: worked out alone why `transaction_id` on Category makes
  duplicate category names; fixed the ERD layout and the per-User uniqueness
  in one round.
- 2026-10-21 — S1.3: predicted that Decimal(0.1) carries the float error before
  running it; chose Numeric scale 2 with a reason.
- 2026-10-22 — S1.4: called is_transfer redundant right away once the link
  column existed; argued two rows beat a transfers table because each Account's
  balance still sums its own rows with no joins.

---

## Hint ladder log

One line per session where a hint was used: `date — session — highest rung — what it was about`.

<!-- newest at the bottom -->
2026-10-20 — S1.1 — L2 — column types and ON DELETE SET NULL (Postgres docs)
2026-10-21 — S1.2 — L2 — why the FK sits on the many side (1NF); DBML composite indexes
2026-10-22 — S1.4 — L2 — self-referencing FK (Postgres constraints docs)

---

## Solo rep log

One entry per `S#.R`: `date — rep — finished? — where I got stuck — what I'd do differently`.

<!-- newest at the bottom -->
