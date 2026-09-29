# Roadmap — Learning Full-Stack by Building the Finance Tracker

A class-style course, 30 minutes a day. Each session is **~10 min concept** (the
what and the why) then **~20 min build**. `PLAN.md` is the design reference;
`DECISIONS.md` is where your reasoning lives; this file is **where we are**.

---

## 📍 You are here

```
Current session:  S0.1 — Git before anything else
Last session:     —
Progress:         0 / 88 sessions
```

Update this block at the end of every session.

---

## How a session works

1. Start by telling Claude "next session". Claude reads this file and opens the
   first unchecked session.
2. **Concept (10m):** Claude explains the idea in a few sentences + one doc link.
   Ask questions until you could explain it to a friend.
3. **Build (20m):** you do the task. Backend and database: **you write every
   line.** Claude asks questions and gives hints, never code.
4. **Check:** show your work. Claude reviews with questions, not fixes.
5. **Close:** tick the box, update "You are here", add one line to the Progress
   log. Commit.

**Rules**

- **Stuck more than 10 minutes?** Write out: what I expected / what happened /
  what I've ruled out. Then ask.
- **Frontend (Stage 5):** Claude writes the React. The session only counts once
  you explain the code back in your own words, or make one small change yourself.
- **New idea mid-session?** It goes in `BACKLOG.md`, not into today.
- **A session can take two days.** 30 minutes is the unit, not the deadline.
  Don't skip the "Done when".
- **Every stage ends with a checkpoint:** explain the stage out loud, update
  `DECISIONS.md`, commit.

---

## The architecture — read this first, re-read at the start of every stage

```
 ┌──────────┐   HTTP + JSON    ┌───────────────────────────── FastAPI ─────────────────────────────┐
 │ Browser  │ ───────────────▶ │  Routes      →   Services / domain   →   Repository   ─────────┐  │
 │ (React)  │ ◀─────────────── │  (HTTP only)     (money logic)          (DB access)            │  │
 └────┬─────┘                  └────────────────────────────────────────────────────────────────┼──┘
      │  login                         ▲ verifies JWT                                            │ SQL
      ▼                                │                                                         ▼
 ┌────────────────┐   issues JWT       │                                          ┌──────────────────────┐
 │ Supabase Auth  │ ───────────────────┘                                          │ Postgres (Supabase)  │
 └────────────────┘                                                               └──────────────────────┘
```

Each box has one job. **Separation of concerns** is the single most important
system design idea: when each part has one job, you can test it, change it, or
replace it without breaking the others.

| Layer | What it does | Why it's separate | What breaks if you merge it |
|---|---|---|---|
| **React (client)** | Shows data, collects input | The UI changes often. Your rules shouldn't change with it. | Business rules live in the browser, where users can edit them. |
| **Routes** | Turn HTTP into function calls and results back into HTTP | HTTP is a *delivery mechanism*, not your app | Logic can only be tested by starting a server |
| **Services / domain** | The money rules: validation, totals, percentages | This is the actual product | Rules get copied into every route and drift apart |
| **Repository** | The only code that talks to the DB | Swap databases, mock in tests, and all the SQL lives in one place | SQL scattered everywhere, and the N+1 bugs hide in it |
| **Postgres** | Stores data durably and enforces constraints | It's the source of truth. It survives restarts and crashes. | — |
| **Supabase Auth** | Proves who the user is (issues a signed token) | Security code is easy to get subtly wrong | — |

**Stateless API:** the FastAPI server keeps nothing in memory between requests.
Everything lives in the DB or the token. That's what lets you later run 5 copies
behind a load balancer (Stage 8).

---

## Stage 0 — Setup & how the web works
**Goal:** a clean repo, and a mental model of what happens when you click a button.
**Interview Q you can answer after:** "What happens when you type a URL and press Enter?"

- [ ] **S0.1 — Git before anything else**
  - *Concept:* Git is a history of snapshots. `.gitignore` goes in **before** the
    first commit, because once a secret is committed it stays in history forever.
  - *Build:* `git init`. Write a `.gitignore` covering `venv/`, `.env`,
    `__pycache__/`, `.pytest_cache/`, `node_modules/`. First commit. Create the
    GitHub repo and push.
  - *Done when:* `git status` is clean and `venv/` is not on GitHub.

- [ ] **S0.2 — Virtual environments & dependencies**
  - *Concept:* A venv gives each project its own copy of its packages, so two
    projects needing different versions don't fight. `requirements.txt` is the
    list of ingredients, so anyone (including a server) can rebuild the same
    environment.
  - *Build:* Activate the venv, `pip install pytest`, `pip freeze > requirements.txt`.
    Delete the venv, recreate it, reinstall from the file.
  - *Done when:* you can rebuild the environment from scratch in under a minute.

- [ ] **S0.3 — The request/response lifecycle**
  - *Concept:* Client/server, DNS, TCP, HTTP request (method, path, headers,
    body), response (status, headers, body). JSON as the shared language.
  - *Build:* Use `curl -v https://api.github.com/users/octocat` and label every
    part of the output on paper: request line, request headers, status, response
    headers, body.
  - *Done when:* you can draw the lifecycle and explain it without notes.

- [ ] **S0.4 — Checkpoint: the 3-tier architecture**
  - *Concept:* Re-read the architecture section above. Presentation / application
    / data tiers.
  - *Build:* Redraw the diagram from memory. Under each box, write one thing it
    must *never* do (e.g. "React never talks to Postgres").
  - *Done when:* diagram committed as `docs/architecture.png` (or `.md`), and you
    can explain why FastAPI sits between React and Supabase (DECISIONS 008).

---

## Stage 1 — Model it on paper (PLAN Phase 0)
**Goal:** know your data before writing code. Changing a drawing is free;
changing a schema with data in it isn't.
**Interview Q:** "Walk me through your data model. Why is it shaped that way?"

- [ ] **S1.1 — Entities, attributes, keys**
  - *Concept:* An entity is a *thing* you store (User, Account, Category,
    Transaction). Primary key = its unique identity. Natural keys (email) vs
    surrogate keys (id). Why every row needs an id that never changes.
  - *Build:* List each entity's fields, types, required/optional, unique.
  - *Done when:* `docs/data-model.md` has all four entities.

- [ ] **S1.2 — Relationships & foreign keys**
  - *Concept:* One-to-many (a User has many Transactions), many-to-many, and
    cardinality. A foreign key is a pointer the DB *guarantees* is valid.
  - *Build:* Draw the ERD with crow's-foot notation (dbdiagram.io or paper).
  - *Done when:* every line has a cardinality and you can say which side holds
    the foreign key.

- [ ] **S1.3 — Money & dates (DECISIONS 001 + 005)**
  - *Concept:* Floats can't represent 0.1 exactly. Integer cents vs `Decimal`. A
    calendar date vs a timestamp with a timezone.
  - *Build:* In a Python shell, prove `0.1 + 0.2 != 0.3`, then prove `Decimal`
    fixes it. Fill in 001 and 005.
  - *Done when:* both are marked `decided`, with reasons.

- [ ] **S1.4 — Transfers & splits (DECISIONS 002 + 004)**
  - *Concept:* Modelling "movement of money" vs "spending". Double-entry intuition.
  - *Build:* Sketch each alternative's tables. Pick one for each. Fill in 002 and 004.
  - *Done when:* you can say why $500 checking→savings doesn't show up as spending.

- [ ] **S1.5 — Delete behaviour & history (DECISIONS 003 + 006 + 007)**
  - *Concept:* `ON DELETE CASCADE` / `SET NULL` / `RESTRICT`. Soft delete. Why
    financial systems avoid destroying history.
  - *Build:* Annotate every FK on your ERD with its on-delete rule. Fill in 003,
    006 and 007.
  - *Done when:* all of DECISIONS 001–007 are `decided`.

- [ ] **S1.6 — Checkpoint**
  - *Build:* Say out loud, without looking, what happens in the DB when you add
    one transaction. Commit the diagram + notes.
  - *Done when:* PLAN Phase 0's "Done when" is met.

---

## Stage 2 — Pure Python domain + pytest (PLAN Phase 1)
**Goal:** the money logic, with no web and no DB, fully tested.
**Interview Q:** "How do you structure code so it's testable?"

- [ ] **S2.1 — Why logic lives alone**
  - *Concept:* Pure functions (same input → same output, no side effects).
    Business logic vs I/O. Why this is the habit that most separates junior from
    senior code.
  - *Build:* Read your current `backend/main.py`. List every place it mixes
    input/printing with logic. Create `backend/domain/` as an empty package.
  - *Done when:* you can point at each line and say "logic" or "I/O".

- [ ] **S2.2 — Your first test**
  - *Concept:* What a unit test is. Arrange / Act / Assert. Why tests are
    documentation that can't go stale.
  - *Build:* Install pytest, write one trivially passing test, run it, then make
    it fail on purpose.
  - *Done when:* you've seen green and red.

- [ ] **S2.3 — The Transaction type**
  - *Concept:* Dataclasses. Representing money per DECISIONS 001. Immutability
    (`frozen=True`) and why it prevents bugs.
  - *Build:* Define `Transaction` and `Category` in `domain/`.
  - *Done when:* you can create one in a test and assert on its fields.

- [ ] **S2.4 — Validation**
  - *Concept:* Fail fast at the boundary. Raise specific exceptions, not
    generic ones.
  - *Build:* Reject zero amounts, missing descriptions, and bad dates. Test each
    rejection with `pytest.raises`.
  - *Done when:* every validation rule has a test.

- [ ] **S2.5 — Categorising**
  - *Build:* Assign and reassign categories. Handle "uncategorised" (per DECISIONS 007).
  - *Done when:* tested, including reassigning to the same category.

- [ ] **S2.6 — Filtering by date range**
  - *Concept:* Inclusive vs exclusive ranges. Why `start <= d < next_month_start`
    avoids the "last day of the month" bug.
  - *Build:* `transactions_between(txns, start, end)`.
  - *Done when:* tests cover the first day, the last day, and just outside each edge.

- [ ] **S2.7 — Totals per category**
  - *Build:* `totals_by_category(txns)` returns category → total.
  - *Done when:* tested with an empty list, a single transaction, and a refund
    (negative amount).

- [ ] **S2.8 — Sorting & percentages**
  - *Concept:* Rounding money. Why percentages don't always add up to 100.
  - *Build:* A sorted summary with percentages.
  - *Done when:* tested, including the rounding edge case.

- [ ] **S2.9 — Fixtures & parametrize**
  - *Concept:* DRY in tests. `@pytest.fixture`, `@pytest.mark.parametrize`.
  - *Build:* Refactor your tests to use both.
  - *Done when:* fewer lines, same coverage, still green.

- [ ] **S2.10 — Checkpoint**
  - *Build:* Delete or rewrite the old CLI loop so it only *calls* the domain.
    Run `pytest --cov` if you like.
  - *Done when:* `pytest` is green and `domain/` imports no web or DB library.
    Commit.

---

## Stage 3 — Persistence (PLAN Phase 2)
**Goal:** data survives a restart, and you understand what the DB does for you.
**Interview Qs:** "What's an index?" "What's the N+1 problem?" "What's a transaction in a DB?" "What's a race condition, and how do you prevent one?"

- [ ] **S3.1 — Why a relational database**
  - *Concept:* Files vs DB. Tables, rows, constraints. The DB enforces rules
    even when your code has bugs. ACID in plain words.
  - *Build:* Create the Supabase project. Find both connection strings (direct vs
    pooled) and note what each is for. Put them in `.env` and confirm `.env` is
    gitignored.
  - *Done when:* you can connect with `psql` or the Supabase SQL editor.

- [ ] **S3.2 — SQL by hand first**
  - *Concept:* DDL vs DML. `CREATE TABLE` with PK, FK, `NOT NULL`, `CHECK`.
  - *Build:* Write the `CREATE TABLE`s for your ERD by hand in the SQL editor.
    Insert 5 rows. Try inserting a bad row and watch it fail.
  - *Done when:* a constraint rejects bad data *you* tried to sneak in.

- [ ] **S3.3 — Queries you'll need**
  - *Build:* Write the SQL for "last month's totals by category" using `JOIN`,
    `WHERE`, `GROUP BY`, `SUM`, `ORDER BY`.
  - *Done when:* the query returns correct numbers for your 5 rows. Save it in
    `docs/queries.sql`. Then drop the tables, because Alembic owns the schema
    from now on.

- [ ] **S3.4 — ORMs: what & why**
  - *Concept:* What an ORM maps (classes ↔ tables). What you gain, and what it
    hides. Engine, Session, connection.
  - *Build:* Install SQLAlchemy + psycopg. Connect and run `SELECT 1` from Python.
  - *Done when:* Python prints 1 from Supabase.

- [ ] **S3.5 — SQLAlchemy models**
  - *Concept:* DB models are *not* domain models (Stage 2). Why keep both.
  - *Build:* Write the models in `backend/db/models.py`, matching the ERD
    (`user_id` everywhere).
  - *Done when:* models import cleanly.

- [ ] **S3.6 — Migrations with Alembic**
  - *Concept:* A migration is version control for your schema. Why you never
    edit production tables by hand.
  - *Build:* `alembic init`. Point it at the **direct** connection string.
    Autogenerate the first migration, **read it**, apply it.
  - *Done when:* tables exist in Supabase and `alembic current` shows your revision.

- [ ] **S3.7 — Rollback**
  - *Build:* `alembic downgrade -1`, then `upgrade head`. Add a column in a second
    migration, then roll it back.
  - *Done when:* upgrade and downgrade both run cleanly, twice.

- [ ] **S3.8 — The repository pattern**
  - *Concept:* One module owns DB access. The domain asks for data; it never
    writes SQL.
  - *Build:* `backend/db/repository.py` with `save_transaction`,
    `get_transactions_between(user_id, start, end)`, and categories CRUD.
  - *Done when:* a script saves a transaction, restarts, and reads it back.

- [ ] **S3.9 — DB transactions (the ACID kind)**
  - *Concept:* Commit / rollback. Atomicity: all or nothing. Why a transfer must
    be one transaction.
  - *Build:* Write a function that saves two rows, and make it crash between
    them. Check that neither was saved.
  - *Done when:* you can show that atomicity worked.

- [ ] **S3.10 — Race conditions & isolation levels**
  - *Concept:* Two requests touch the same row at the same time. Lost update,
    dirty/non-repeatable reads. Isolation levels (Read Committed is the Postgres
    default, then Repeatable Read, then Serializable). Pessimistic locking with
    `SELECT ... FOR UPDATE`.
  - *Build:* Open two SQL sessions side by side. Reproduce a lost update by hand
    (both read, both write, one write vanishes). Then prevent it with
    `FOR UPDATE` and watch session 2 wait.
  - *Done when:* you can draw the timeline of both sessions and point to where
    the update was lost.

- [ ] **S3.11 — Indexes**
  - *Concept:* A B-tree index lets the DB jump to the matching rows instead of
    scanning the whole table. It speeds reads and costs writes. The summary query
    filters by `user_id` + date.
  - *Build:* Seed 10k rows, run `EXPLAIN ANALYZE` on your summary query, add a
    composite index via a migration, run it again.
  - *Done when:* you can explain why the plan changed (Seq Scan → Index Scan).

- [ ] **S3.12 — The N+1 problem**
  - *Concept:* 1 query for the list + N queries for each item's related data.
    Invisible in dev, slow in prod.
  - *Build:* Turn on SQL logging (`echo=True`), load 100 transactions, print each
    category name, count the queries. Fix it with `selectinload` / `joinedload`.
  - *Done when:* 101 queries become 1 or 2.

- [ ] **S3.13 — Checkpoint: RLS + review**
  - *Concept:* Row-level security as defense in depth.
  - *Build:* Enable RLS on every table in Supabase. Update DECISIONS with
    anything you changed.
  - *Done when:* restart everything and the data is still there, and migrations
    roll back and forward cleanly. Commit.

---

## Stage 4 — The REST API (PLAN Phase 3)
**Goal:** a clean, tested HTTP API. **This is the core of the job you want.**
**Interview Qs:** "Design a REST API for X." "PUT vs PATCH?" "What status code for…?" "How do you test an API?"

- [ ] **S4.1 — What REST is**
  - *Concept:* Resources (nouns) + HTTP verbs. Statelessness. URLs name *things*,
    verbs say *what to do*. `/getTransactions` is a smell.
  - *Build:* On paper, design every endpoint for this app (compare with PLAN
    Phase 3 *after*).
  - *Done when:* your list matches or beats PLAN's, and you can justify the differences.

- [ ] **S4.2 — Status codes & idempotency**
  - *Concept:* 2xx/4xx/5xx. 200 vs 201 vs 204. 400 vs 404 vs 409 vs 422.
    Idempotent = safe to retry (GET, PUT, DELETE yes; POST no). Why that matters
    on flaky networks.
  - *Build:* Next to each endpoint from S4.1, write its success and failure codes.
  - *Done when:* every endpoint has codes, and you can say which are idempotent.

- [ ] **S4.3 — Hello FastAPI**
  - *Concept:* ASGI server (uvicorn) vs framework (FastAPI). What `/docs` is
    (OpenAPI).
  - *Build:* `backend/api/main.py` with `GET /api/health` → `{"status": "ok"}`.
    Run it and hit it from `/docs` and from `curl`.
  - *Done when:* both work.

- [ ] **S4.4 — Pydantic schemas**
  - *Concept:* Schemas are the API's *contract*. The shape you accept
    (`TransactionCreate`) ≠ the shape you return (`TransactionOut`) ≠ the DB
    model. Why: never leak internal fields, and never let the client set `id` or
    `user_id`.
  - *Build:* `backend/api/schemas.py` for categories and transactions.
  - *Done when:* you can explain why there are three shapes for one thing.

- [ ] **S4.5 — Categories endpoints**
  - *Build:* `GET` and `POST /api/categories`, calling the repository.
  - *Done when:* you create and list categories through `/docs`, with 201 on create.

- [ ] **S4.6 — Dependency injection**
  - *Concept:* `Depends()`. Handing a route its DB session instead of letting
    it create one. Why: testability, and one session per request.
  - *Build:* Write a `get_db` dependency. Refactor S4.5 to use it.
  - *Done when:* no route creates its own session.

- [ ] **S4.7 — Transactions: create & read**
  - *Build:* `POST /api/transactions` and `GET /api/transactions?start=&end=`.
  - *Done when:* bad input gets 422 automatically, and you know why.

- [ ] **S4.8 — Update & delete**
  - *Concept:* PUT (replace) vs PATCH (partial update). 404 for a missing id.
  - *Build:* `PATCH` and `DELETE /api/transactions/{id}`.
  - *Done when:* PATCH changes one field only, and DELETE returns 204, then 404
    on a repeat.

- [ ] **S4.9 — Optimistic concurrency**
  - *Concept:* Locks are pessimistic. Optimistic concurrency instead adds a
    `version` column, and an update only succeeds if the version still matches.
    409 Conflict. ETags / `If-Match`, the HTTP version of the same idea.
  - *Build:* A migration adding `version`. PATCH requires the current version
    and bumps it. A test fires two PATCHes with the same version.
  - *Done when:* the second PATCH gets 409 instead of silently overwriting, and
    you can say when you'd pick optimistic vs `FOR UPDATE`.

- [ ] **S4.10 — The service layer**
  - *Concept:* Routes stay thin (≤10 lines): parse → call service → return.
  - *Build:* Move any logic that crept into routes into `backend/services/`.
  - *Done when:* no route has an `if` about money.

- [ ] **S4.11 — The summary endpoint**
  - *Build:* `GET /api/summary?month=2026-09`, using the Stage 2 domain functions.
  - *Done when:* it matches your hand-written SQL from S3.3 on the same data.

- [ ] **S4.12 — Error handling**
  - *Concept:* Consistent error bodies. Domain exceptions → HTTP codes at *one*
    place (exception handlers). Never leak stack traces.
  - *Build:* Map your domain exceptions to 400/404/409.
  - *Done when:* every error response has the same JSON shape.

- [ ] **S4.13 — Pagination & filtering**
  - *Concept:* Why you never return an unbounded list. Offset vs cursor pagination.
  - *Build:* Add `limit`/`offset` (with a max) to the transactions list.
  - *Done when:* `?limit=10000` gets capped.

- [ ] **S4.14 — API tests**
  - *Concept:* Integration tests vs unit tests. The test pyramid. A separate test
    DB, or overriding dependencies.
  - *Build:* `TestClient` tests for the happy path + one failure per endpoint.
  - *Done when:* `pytest` covers the domain *and* the API, green.

- [ ] **S4.15 — Checkpoint: CORS + a month of data**
  - *Concept:* Same-origin policy. Why the browser, not the server, blocks
    requests. Preflight `OPTIONS`.
  - *Build:* Add CORS middleware allowing `http://localhost:5173` only. Enter a
    real month of spending via `/docs`.
  - *Done when:* PLAN Phase 3's "Done when" is met. Commit.

---

## Stage 5 — React frontend (PLAN Phase 4)
**Goal:** understand how a client consumes *your* API. Claude writes it; you
explain every file back.
**Interview Q:** "How does your frontend talk to your backend? What happens when the API is down?"

- [ ] **S5.1 — Vite + React scaffold**
  - *Concept:* SPA vs server-rendered pages. What Vite does. `npm` = `pip` for JS.
  - *Claude builds:* `frontend/` scaffold. *You:* run it, and explain the folder
    structure and what `main.jsx` does.
  - *Done when:* you can explain each file Vite created.

- [ ] **S5.2 — Components & state**
  - *Concept:* A component is a function that returns UI. Props vs state.
    Re-render on state change.
  - *Claude builds:* a static transactions table. *You:* add a column yourself.
  - *Done when:* you explain props vs state in your own words.

- [ ] **S5.3 — Fetching from your API**
  - *Concept:* `fetch`, promises/async, `useEffect` and its dependency array.
    StrictMode double-running effects.
  - *Claude builds:* load transactions from `/api/transactions`. *You:* watch the
    request in the browser DevTools Network tab and match it to your FastAPI log.
  - *Done when:* you can trace one click end-to-end through both sides.

- [ ] **S5.4 — Loading & error states**
  - *Claude builds:* spinner/error UI. *You:* stop the API and explain what the
    user sees and why.
  - *Done when:* you can name all three states of a request.

- [ ] **S5.5 — The add-transaction form**
  - *Concept:* Controlled inputs. POST from the browser. Showing 422 errors to
    the user.
  - *Claude builds:* the form. *You:* add client-side validation for one field,
    and explain why the server *still* validates.
  - *Done when:* the list updates after adding.

- [ ] **S5.6 — Edit & delete**
  - *Claude builds:* edit/delete buttons. *You:* explain optimistic vs
    pessimistic UI updates.
  - *Done when:* explained.

- [ ] **S5.7 — Summary view + chart**
  - *Claude builds:* summary page with Recharts. *You:* change the month picker
    behaviour yourself.
  - *Done when:* the chart matches `/api/summary`.

- [ ] **S5.8 — Checkpoint**
  - *Build:* Make it look decent. Enter a month of data without touching `/docs`.
  - *Done when:* PLAN Phase 4's "Done when" is met. Commit.

---

## Stage 6 — Auth & multi-tenancy (PLAN Phase 5)
**Goal:** many users, each seeing only their own money.
**Interview Qs:** "Authentication vs authorization?" "How does a JWT work?" "What's an IDOR?"

- [ ] **S6.1 — Authn vs authz**
  - *Concept:* Who you are vs what you're allowed to do. Sessions vs tokens.
  - *Build:* Write a paragraph in `docs/auth.md` explaining both, using this app.
  - *Done when:* written.

- [ ] **S6.2 — JWTs**
  - *Concept:* Header.payload.signature. Base64 is *not* encryption. Signing
    proves the token wasn't tampered with. Expiry.
  - *Build:* Decode a sample JWT at jwt.io by hand. Change one character and
    watch the signature fail.
  - *Done when:* you can explain why a user can't just edit their `user_id` in
    the token.

- [ ] **S6.3 — Supabase Auth setup**
  - *Build:* Enable email auth, create two test users, and get a token for each
    (Claude wires the React login in this session).
  - *Done when:* you have two real tokens.

- [ ] **S6.4 — The verification dependency**
  - *Concept:* JWKS / signing keys, audience, expiry checks.
  - *Build:* Write `get_current_user` — decode, verify the signature, check
    expiry, return the user id. **You write this.**
  - *Done when:* a bad or expired token gets 401.

- [ ] **S6.5 — Scope every query**
  - *Build:* Every route uses `get_current_user`, and every repository query
    filters by that user id.
  - *Done when:* grep finds no query without `user_id`.

- [ ] **S6.6 — The IDOR attack**
  - *Concept:* Insecure Direct Object Reference: changing an id in the URL to
    read someone else's data.
  - *Build:* As user A, try to GET, PATCH and DELETE user B's transaction by id.
  - *Done when:* all three return 404 (not 403, and know why).

- [ ] **S6.7 — Auth tests**
  - *Build:* Tests for no token, a bad token, and a cross-user access attempt.
  - *Done when:* green.

- [ ] **S6.8 — Checkpoint**
  - *Build:* Update DECISIONS: why the user id comes from the token, never the body.
  - *Done when:* explained out loud. Commit.

---

## Stage 7 — Ship it (PLAN Phase 6 + operations)
**Goal:** a real URL, deployed automatically, that you can watch.
**Interview Qs:** "How do you deploy?" "What's in your CI?" "How would you know if prod was broken?"

- [ ] **S7.1 — Config & secrets**
  - *Concept:* 12-factor config. Env vars. Why the same code runs in dev and prod.
  - *Build:* A settings module (pydantic-settings) that reads everything from the
    environment. Add `.env.example`.
  - *Done when:* no secret or URL is hard-coded.

- [ ] **S7.2 — Docker: what & why**
  - *Concept:* Image vs container. "It works on my machine", solved.
  - *Build:* Write a Dockerfile for the API. Build it and run it locally.
  - *Done when:* the API runs in a container, hitting Supabase.

- [ ] **S7.3 — Deploy the API**
  - *Build:* Deploy to Railway, Render or Fly.io. Set the env vars there.
  - *Done when:* `/api/health` responds on a public URL.

- [ ] **S7.4 — Migrations on deploy**
  - *Concept:* Schema changes must ship *with* the code, and be
    backward-compatible for a moment.
  - *Build:* Run `alembic upgrade head` as a release step.
  - *Done when:* a new migration applies itself on deploy.

- [ ] **S7.5 — Deploy the frontend**
  - *Build:* Static build to Vercel, Netlify or Cloudflare Pages. Update CORS to
    the real domain.
  - *Done when:* the live site talks to the live API.

- [ ] **S7.6 — CI with GitHub Actions**
  - *Concept:* Continuous integration: every push is tested automatically.
  - *Build:* A workflow that runs `pytest` on each push and PR.
  - *Done when:* a deliberately broken test turns the PR red.

- [ ] **S7.7 — Logging**
  - *Concept:* Structured logs, log levels, request ids. Never log tokens or amounts
    tied to users.
  - *Build:* Add request logging middleware with a request id.
  - *Done when:* you can find one request's full story in the platform's logs.

- [ ] **S7.8 — Health checks & keeping it awake**
  - *Concept:* Liveness vs readiness. Why Supabase free tier pauses.
  - *Build:* `/api/health` also checks the DB. Schedule a ping (cron or GitHub
    Action).
  - *Done when:* the site is awake after a week away.

- [ ] **S7.9 — Checkpoint**
  - *Build:* Draw the *deployed* architecture (domains, services, where secrets live).
  - *Done when:* the URL is on your résumé. Commit.

---

## Stage 8 — Scaling *this* app (system design, applied)
**Goal:** understand what changes at 1,000× users, by actually doing it to your app.
**Interview Q:** "How would you scale your app?" You'll answer from experience, not theory.

- [ ] **S8.1 — Back-of-envelope estimates**
  - *Concept:* Estimating QPS, storage, and read/write ratio. Where the bottleneck
    is *first*.
  - *Build:* In `docs/scaling.md`, estimate the numbers for 100k users entering
    3 transactions/day.
  - *Done when:* you know if you're read-heavy or write-heavy, and why it matters.

- [ ] **S8.2 — Load testing**
  - *Concept:* Latency vs throughput, p50/p95/p99.
  - *Build:* A `locust` script hitting `/summary` and `POST /transactions`.
  - *Done when:* you have baseline p95 numbers written down.

- [ ] **S8.3 — Stateless & horizontal scaling**
  - *Concept:* Vertical (bigger box) vs horizontal (more boxes). Load balancers.
    Why statelessness makes horizontal scaling easy.
  - *Build:* Run 2 API instances locally behind a simple proxy (or 2 replicas on
    your host). Check that nothing breaks.
  - *Done when:* you can explain what *would* break if you stored anything in memory.

- [ ] **S8.4 — Concurrency inside the server**
  - *Concept:* Processes vs threads vs async. The event loop. `async def` vs
    `def` in FastAPI (a threadpool runs the plain `def` routes). Why one blocking call
    inside `async def` freezes every request. The GIL in plain words.
  - *Build:* Add a test route with `time.sleep(2)` in an `async def`, load-test
    it, then fix it (plain `def` or `asyncio.sleep`) and load-test again.
  - *Done when:* you can explain the difference in the numbers and answer
    "threads vs async?" without notes.

- [ ] **S8.5 — Connection pooling**
  - *Concept:* DB connections are expensive and limited. Pooler vs direct
    (remember S3.1).
  - *Build:* Switch the app to the pooled connection string, tune the pool size,
    and re-run the load test.
  - *Done when:* you can explain what happens at 10 instances × 20 connections.

- [ ] **S8.6 — Caching the summary**
  - *Concept:* Cache-aside. TTL. "There are only two hard things…" Where caches
    live (in-process vs Redis).
  - *Build:* Cache `/summary` per user+month in Redis (Upstash free tier).
  - *Done when:* p95 drops, and you measured it.

- [ ] **S8.7 — Cache invalidation**
  - *Build:* A new or edited transaction invalidates that month's cache entry.
    Write a test that proves stale data can't be served.
  - *Done when:* the test is green.

- [ ] **S8.8 — Rate limiting**
  - *Concept:* Token bucket. Protecting the API from abuse and from your own
    frontend bugs. 429.
  - *Build:* Per-user rate limit on write endpoints.
  - *Done when:* hammering the endpoint returns 429.

- [ ] **S8.9 — Background jobs (CSV import)**
  - *Concept:* Why slow work leaves the request/response cycle. Queues and
    workers. 202 Accepted + a status endpoint.
  - *Build:* Pull "Bank CSV import" from BACKLOG. Upload → job → worker parses
    and inserts.
  - *Done when:* uploading a 5k-row CSV returns instantly and finishes in the background.

- [ ] **S8.10 — Idempotency keys**
  - *Concept:* A double-click or a network retry must not create two
    transactions. How Stripe does it.
  - *Build:* Support an `Idempotency-Key` header on `POST /transactions`.
  - *Done when:* sending the same request twice creates one row.

- [ ] **S8.11 — Checkpoint: observability & the design doc**
  - *Concept:* Metrics, logs, traces: the three pillars.
  - *Build:* Finish `docs/scaling.md` as a mini design doc: the current
    architecture, bottlenecks found, what you changed, what you'd do next
    (read replicas, sharding by user_id) and *why not yet*.
  - *Done when:* you can whiteboard it in 10 minutes. Commit.

---

## Stage 9 — Job-ready
**Goal:** turn the project into interviews.

- [ ] **S9.1 — README**
  - *Build:* A README with what it does, the architecture diagram, how to run it,
    key decisions (linking DECISIONS.md), the live URL, and screenshots.
  - *Done when:* a stranger could run it locally.

- [ ] **S9.2 — The 5-minute walkthrough**
  - *Build:* Record yourself explaining the app, one request's journey, and one
    hard decision.
  - *Done when:* you watch it back and would hire yourself.

- [ ] **S9.3 — System design mock**
  - *Build:* Claude interviews you: "Design a personal finance app for 1M users."
    You answer using *your* app.
  - *Done when:* you drive the whole conversation.

- [ ] **S9.4 — Stage-by-stage question drill**
  - *Build:* Answer every "Interview Q" in this file out loud.
  - *Done when:* no answer needs notes. 🎓

---

## Progress log

One line per session: `YYYY-MM-DD — S#.# — what I learned / built`

<!-- newest at the bottom -->
