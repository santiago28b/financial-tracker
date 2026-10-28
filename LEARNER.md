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
- 2026-10-23 — S1.5: line 1 was a real requirement; lines 2–3 had the FK
  direction backwards and named a solution ("updated"). Fixed both after one
  question each. Asked "what specifically do you want me to do" twice; a filled-in
  template unblocked it each time.
- 2026-10-25 — S2.2 (min): "i dont know you tell what do you want me to test";
  a fill-in-the-blanks template unblocked it in one round. Then the first code
  was the pytest docs example, not the planned test_addition; rewrote it to match.
- 2026-10-26 — S2.3: ritual line 1 named the tool ("they'll be dataclasses")
  instead of a requirement; field list was right. Skipped the failing test for
  4 review rounds; the fill-in template got it written. Once it existed, every
  later bug showed up in the test output instead of in review.
- 2026-10-27 — S2.4: ritual line 1 mixed requirements with solutions
  ("auto-generate dates", an income/spend enum); sorted after one round. Wrote
  the failing zero-amount test before any code (first time without a template),
  but first copied the docs shape (`int(0)`) inside pytest.raises. Date test and
  fix were written together; says the red was seen but not shown.
- 2026-10-28 — S2.5: ritual lines 1–2 were real requirements (no tools named) but
  said the same thing, and uncategorised was missing; signature planned "return
  void, modify it" despite frozen. One round of 3 questions fixed all of it.
  Wrote the description tests first; red runs shown twice, skipped once.

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
- 2026-10-23 — S1.5: got tired mid-build and asked Claude to write the DBML
  ("just do it, I'm tired of typing"). When offered a stop, chose to push through
  and finished. Needed a concrete example (L3) for DBML Ref syntax; took 3 rounds.
- 2026-10-25 — S2.2 (min): hit "fixture 'x' not found"; pasted the error but
  didn't write expected / actual / ruled out. Kept going after L1 → L2.
- 2026-10-26 — S2.3: long session, kept going through ~10 red runs. Started
  guessing near the end (`backend`, then `tests` for the path) and moved fields
  one line at a time instead of using the rule. Said "I don't know what you're
  talking about" once; L3 plain-English layout unblocked it. Didn't read the
  pytest warning until shown where it was.
- 2026-10-27 — S2.4: "I have no idea" on the first warm-up prediction; a nudge
  got a correct guess with the right reason. Didn't know the expected / actual /
  ruled out drill by name. Fixed the import error alone once asked where
  pytest.ini lives. No giving up across ~8 red runs.
- 2026-10-28 — S2.5: misread `DID NOT RAISE` as "it raised both errors". Changed a
  test from TypeError to ValueError to make it green, and said so when asked.
  Asked for help ("don't quite understand the tests") instead of stalling; a
  fill-in template unblocked it. No giving up.

### 3. Consistency
Drill: 30–45 min daily; a 10-minute **minimum session** counts on bad days.
Streak lives in ROADMAP "You are here".
Evidence:
- 2026-09-28 → 2026-10-20 — 3-week gap after S0.3 (classes).
- 2026-10-20 — back: S0.4 done in one sitting.
- 2026-10-20 — took a minimum session instead of skipping the day.
- 2026-10-20 — then turned it into a full 45-min S1.1.
- 2026-10-23 — S1.5: 4-day streak. Finished the session while tired instead of
  stopping.
- 2026-10-24 — S1.6: did a minimum session instead of skipping; 5-day streak.
- 2026-10-25 — S2.2: minimum session again; 6-day streak.

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
- 2026-10-23 — S1.5: asked Claude to write 003/006 again. Dictated 006; 003
  pasted from what I'd said earlier. Neither Why names what is given up (003:
  grouping; 006: any record of the old amount). Explained the counterpart
  cascade line correctly.
- 2026-10-24 — S1.6 (min): explained the ERD from memory. First pass had the FK
  backwards ("account has a transaction ID") and called the checked tables
  "touched"; fixed both after one question each. Gave the −12 sign rule from
  own notes with the reason.
- 2026-10-24 — S2.1 (min): labelled per function first, then per line after
  being asked. Fixed line 3 (append = logic); line 8 still only says "logic"
  though it's also I/O. Created `__init__.py` without knowing why ("no idea");
  given the answer (regular package) at L2.
- 2026-10-25 — S2.2 (min): committed to the docs example (`func`, `test_answer`)
  first; didn't know Arrange / Act / Assert when asked to point at them. After
  rewriting, saw why `assert ans == x+y` can't catch a broken `+`, and changed it to `== 8`.
- 2026-10-26 — S2.3: copied `python_files` from the pytest docs thinking it set
  imports. Made tests green by moving lines and flipping an assert, while
  `account_id`/`user_id` still had random defaults; explained it correctly when
  asked in words. Explained `default_factory=uuid4` vs `uuid4()` (called at
  creation vs once). 012's Why ("easier, efficient, not a security risk") is
  thin: it doesn't name the real gain (frozen + never None).
- 2026-10-27 — S2.4: asked to understand the warm-up lines before writing code
  (unprompted). Explained `as e` (partly: it's the whole error object) and why
  TransactionError works below __post_init__ (method runs at call time).
  DECISIONS 013 (description optional) still to write.
- 2026-10-28 — S2.5: dictated 013 (decision, why, given up) in own words over 3
  prompts; Given up named the real cost this time. Explained `self is first`
  passes only because of the `if`, since replace makes a new object.

### 5. Python language mechanics
Self-reported 2026-10-26 after S2.3: "I have a hard time trying to understand
Python here." Function vs call (`uuid4` vs `uuid4()`), when defaults are
evaluated, type hints not enforced, import paths.
Drill: the Stage 2 **Python warm-up** (ROADMAP): 5 minutes in the shell before
the ritual, predicting then running the one mechanic the build uses. When the
concept is Python itself rather than design, Claude shows it in the shell first.
Evidence:
- 2026-10-26 — S2.3: passed `uuid4` as a value (stored the function as the id);
  then `default_factory=uuid4()`; predicted `= uuid4()` runs once per object.
  Treated "type hint" and "default" as the same thing (added `default_factory`
  when asked for `UUID`). Didn't know `.` means "this folder". All fixed by the
  end, and the uuid4 vs uuid4() difference was explained back in own words.
- 2026-10-27 — S2.4: predicted "empty class does nothing" for `MyError(ValueError)`;
  then got "a child is caught by except ValueError" right. Put `raise` inside a
  class body (NameError); used `default_factory=''`; again read `str | None` as
  making a field optional (hint vs default). Called `date` a keyword (it's a
  shadowed name). Got `default_factory=date.today` vs `date.today()` right and
  explained it back. Decimal(0.1) vs Decimal("0.1") predicted wrong, shell fixed it.
- 2026-10-28 — S2.5: warm-up 2/3 (thought replace leaves b = 1), then explained
  replace correctly. Put `;TypeError` on the import line to "use it" (built-ins
  need no import). Thought `self` in a method is the blueprint, not the object.
  Wrote `replace(self, self.category_id=...)`. Two tests with the same name, so one
  silently didn't run; caught it from the count when asked.

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
- 2026-10-23 — S1.5: traced the delete chain once asked: User CASCADE → Account
  → Transactions RESTRICT fails, so Transactions must cascade since day-to-day
  Account removal is a soft delete. Spotted the missing counterpart column myself.
- 2026-10-24 — S1.6 (min): explained the insert path from memory; fixed "only
  transactions is written, the other two are checked" after one question.
- 2026-10-24 — S2.1: explained in own words why process_info isn't pure (it
  mutates a list it doesn't own); saw that `process_info()` with no args raises
  TypeError.
- 2026-10-25 — S2.2: worked out why pytest ran 2 tests (both names start with
  test_), and that a fixture is something pytest supplies.
- 2026-10-26 — S2.3: asked the right question unprompted ("why doesn't
  account_id have a default if it's also a UUID?") and answered that the caller
  passes it, not the class. Pushed through a long red streak to green.
- 2026-10-27 — S2.4: read the __post_init__ docs and summarised them correctly
  on first try; fixed the ValueError inheritance by applying the warm-up alone;
  spotted the `date` name clash and renamed the field without being asked.
- 2026-10-28 — S2.5: asked unprompted what happens to the old Transaction after
  replace (memory vs DB row); predicted the transaction_id stays the same and
  proved it with an assert.

---

## Hint ladder log

One line per session where a hint was used: `date — session — highest rung — what it was about`.

<!-- newest at the bottom -->
2026-10-20 — S1.1 — L2 — column types and ON DELETE SET NULL (Postgres docs)
2026-10-21 — S1.2 — L2 — why the FK sits on the many side (1NF); DBML composite indexes
2026-10-22 — S1.4 — L2 — self-referencing FK (Postgres constraints docs)
2026-10-23 — S1.5 — L3 — DBML Ref syntax with [delete: ...] and a self-reference (books/sequel_of example)
2026-10-24 — S1.6 — L1 — FK direction and written vs checked tables on insert
2026-10-24 — S2.1 — L2 — why a package needs __init__.py (Python tutorial, Packages)
2026-10-25 — S2.2 — L2 — test parameters are read as fixtures (pytest fixtures docs)
2026-10-26 — S2.3 — L3 — dataclass field ordering (required on top, defaults at the bottom); L2 default_factory and pytest pythonpath
2026-10-27 — S2.4 — L2 — __post_init__ (dataclasses docs), pytest.raises shape (pytest docs), user-defined exceptions
2026-10-28 — S2.5 — L2 — dataclasses.replace and `self` is the instance; built-in exceptions need no import; fill-in test template

---

## Solo rep log

One entry per `S#.R`: `date — rep — finished? — where I got stuck — what I'd do differently`.

<!-- newest at the bottom -->
