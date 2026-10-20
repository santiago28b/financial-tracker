# Finance Tracker — Build Plan

Daily sessions and progress: see [ROADMAP.md](ROADMAP.md).

Living version (editable, commentable): https://claude.ai/code/artifact/674bebd1-2b30-4c12-9916-eb7da1171c8d

---

## Scope: what v1 is

One question, answered well: **where did my money go last month?**

v1 ships when you can type in a transaction, tag it with a category, and see a
breakdown of last month's spending. That's it.

In scope:

- Manual transaction entry (date, amount, description, category)
- A fixed set of categories you define
- Monthly spending breakdown, by category
- One hardcoded user

Explicitly not in v1 — write these down so you stop yourself drifting:

- Bank CSV import
- Budgets and limits
- Net worth and account balances
- Forecasting
- Real signup and login (design for it now, build it in Phase 5)
- Mobile, dark mode, or anything cosmetic

The discipline matters more than the list. Personal projects die from scope
creep, not from difficulty. Every new idea goes in `BACKLOG.md`, not into the
current phase.

---

## The stack, and why

| Layer | Choice | Why |
| --- | --- | --- |
| Backend | FastAPI | Auto-generated API docs you can click through to test, and Pydantic forces you to think in data shapes. |
| Database | Supabase (hosted Postgres) | It's just Postgres, so SQLAlchemy and Alembic work unchanged — and no Docker setup before you write a line of real code. |
| Auth | Supabase Auth | The one piece not worth hand-rolling for an app holding real financial data. You still write the JWT verification middleware yourself. |
| ORM | SQLAlchemy + Alembic | Learn migrations while the schema is small enough to break safely. |
| Frontend | React + Vite | You want to learn frontend. This is the version employers ask about. |
| Hosting | Railway, Render, or Fly.io | All take a Dockerfile and have a free-ish tier. |

**On Streamlit:** right tool for "I just want to see my data," wrong tool for
this. Single-user, re-runs the whole script on every interaction, no real
routing or auth story, and nothing you learn transfers. Skip it.

**On Next.js:** not yet. Learn React and HTTP first, not a framework's
conventions layered on top of them.

**On Supabase:** used as hosted Postgres + an auth provider *behind* your own
FastAPI — not as the whole backend. React talks to your API; your API talks to
Supabase. Letting React talk to Supabase directly is faster but skips the
backend, which is most of what you wanted to learn.

Free-tier projects pause after about a week without database activity. Data
survives and you can resume from the dashboard, but a portfolio link will be
asleep exactly when someone clicks it. Ping it on a schedule or budget for the
paid tier before the URL goes anywhere.

---

## Build order at a glance

1. **Phase 0** — model it on paper
2. **Phase 1** — pure Python logic + pytest
3. **Phase 2** — Supabase project, SQLAlchemy, Alembic
4. **Phase 3** — FastAPI
5. **Phase 4** — React
6. **Phase 5** — Supabase Auth + JWT verification
7. **Phase 6** — deploy
8. **Phase 7** — AI features (auto-categorize, then an "ask your money" agent)

The one that's easy to get wrong: **the database comes before the frontend, not
after.** Login can wait until the end, but persistence can't — a frontend built
against an API with nowhere to put data gets built twice.

---

## Phase 0 — model it on paper

No code. Probably an hour, and it's the highest-leverage hour in the project.

Draw the entities and the lines between them:

- **User** — owns everything else
- **Account** — checking, savings, a credit card. Even in v1 where you only have
  one, having the table means transfers work later.
- **Category** — groceries, gas, rent
- **Transaction** — belongs to an account, has a category, an amount, a date, a
  description

For each entity: what fields, what types, what is required, what is unique. For
each line between two entities: which side owns the relationship, and what
happens on delete.

Output is a diagram and a page of notes, checked into the repo.

**Done when:** you can explain out loud, without looking, what happens in the
database when you add one transaction.

---

## Phase 1 — pure Python, no web, no database

This is where the actual skill-building happens. Give it real time.

A module that knows about money and nothing else. No Flask, no SQL, no HTTP:

- Create a transaction and validate it
- Assign and reassign categories
- Given a list of transactions and a date range, return totals per category
- Sort those totals, work out percentages

Test it with **pytest**. Actual tests, including the annoying cases: empty
month, a single transaction, a refund (negative expense), a transaction on the
first and last day of the month.

Why separate it out: logic that lives inside route handlers can't be tested
without a server and can't move when you change frameworks. This is the single
habit that most separates junior code from senior code.

**Done when:** `pytest` is green and you have never imported a web framework.

---

## Phase 2 — persistence

Now the data survives restarting the program. With Supabase this is mostly
configuration rather than setup.

1. Create the Supabase project. Do this now even though auth is Phase 5 — you
   need the connection string here anyway.
2. SQLAlchemy models matching the Phase 0 diagram
3. Alembic set up, first migration generated and applied against Supabase
4. A thin layer between logic and database — `save_transaction`,
   `get_transactions_between(start, end)`. Your logic calls these; it never
   writes SQL itself.

**The connection string gotcha:** Supabase gives you two. Alembic migrations
want the *direct* connection, not the pooled one — the pooler doesn't handle
long-lived transactions the same way, and the error when you get this wrong is
not obvious.

Two things to force yourself to learn here:

- **Indexes.** The main query filters by user and date range. Index those
  columns and understand why it changes anything.
- **The N+1 problem.** Load 100 transactions, ask each for its category name,
  and you've made 101 queries. Find out how SQLAlchemy avoids this
  (`joinedload` / `selectinload`).

**Row-level security:** with FastAPI as the gatekeeper you don't strictly need
it. Turn it on anyway — defense in depth, genuinely interesting, and it means a
bug in your API isn't automatically a data breach.

**Done when:** you can restart everything and the data is still there — and a
migration rolls back and re-applies cleanly.

---

## Phase 3 — the API

FastAPI on top of what you already built. Route handlers stay thin — parse,
call your Phase 1 logic, return. More than ten lines means logic has leaked in.

```
GET    /api/categories
POST   /api/categories
GET    /api/transactions?start=&end=
POST   /api/transactions
PATCH  /api/transactions/{id}
DELETE /api/transactions/{id}
GET    /api/summary?month=2026-09
```

That last one is the whole product in one endpoint.

- **Pydantic schemas separate from DB models.** What the API accepts is not the
  shape the database stores, and conflating them leaks internal fields.
- **Status codes that mean something.** 201 on create, 404 on missing, 422 on
  invalid input.
- **CORS**, because your React dev server is on a different port. Expect to lose
  an hour to this the first time.

**Done when:** you can do a full month of data entry through `/docs` alone.

---

## Phase 4 — React, built ugly first

No styling at all to start. A table and a form.

1. **A table listing transactions**, fetched with `fetch` in a `useEffect`
2. **A form that adds one**, and the list updating afterwards
3. **Loading and error states** — the step everyone skips. What shows while the
   request is in flight, and when the API is down?
4. **The summary view**, with a chart (Recharts)
5. **Then** make it look decent

No Redux, no Zustand, no component library. `useState` and `useEffect` carry an
app this size; reaching for a state library before feeling the pain it solves
means you won't understand what it does.

React 18's StrictMode runs effects twice in development. When your transaction
appears twice, that's why — and it's telling you something real about the code.

**Done when:** you can add and view a month of spending without touching `/docs`.

---

## Phase 5 — auth and multi-tenancy

Build last, design for from Phase 0. Put `user_id` on every table now, while
you're the only user. Retrofitting means touching every query you've written.

Supabase Auth handles signup, login, password resets and email verification.
You handle the part that matters: **the verification middleware.** Decode the
incoming JWT, validate the signature against Supabase's public key, pull the
user ID out, attach it to the request. Roughly thirty lines, and it's where
auth actually becomes real to you.

The rule people get wrong, and the reason that middleware matters: **the user ID
comes from the verified token, never from the request body or a URL parameter.**
If your endpoint is `GET /api/transactions?user_id=5`, anyone reads anyone's
finances by changing a number. Supabase handing you a valid token doesn't stop
you writing that bug.

What you're choosing not to learn: bcrypt, session design, token refresh flows.
A real gap but a narrow one, and every job you'd take uses a provider anyway.
If it bothers you, build auth by hand once on a throwaway project some weekend.

---

## Phase 6 — deploy

Dockerfile for the API, static build for React, database already live on
Supabase.

- Secrets in environment variables. Add `.env` to `.gitignore` before your first
  commit, not after.
- Running migrations on deploy
- CORS again, now with real domains

Then put the URL and the repo on your résumé. One deployed app you can talk
through in detail beats three half-finished ones.

---

## Phase 7 — AI features

Two features on top of the deployed app (DECISIONS 009–010):

- **Auto-categorize:** a new Transaction without a Category gets one suggested
  by an LLM, as validated structured output with a confidence score. Low
  confidence stays uncategorised; a User's correction always wins; if the LLM is
  down, the Transaction still saves.
- **"Ask your money" agent:** a question like "why was October higher?" is
  answered by an LLM that calls your own service functions as tools. The User id
  comes from the JWT, never from the model.

The part that makes it portfolio-worthy is the **eval set**: 50 labelled
Transactions, an accuracy score, before/after numbers for each prompt change,
and CI failing if accuracy drops. You write all of it; the AI feature falls
under the same rule as the rest of the backend.

**Done when:** you can show the accuracy number, the cost per request, and
whiteboard the agent loop with its trust boundaries.

---

## Design traps — settle these before Phase 1

Each one belongs in `DECISIONS.md` with your answer and your reasoning.

**Never use floats for money.** `0.1 + 0.2 != 0.3` in binary floating point.
Store integer cents, or Python's `Decimal` with Postgres `Numeric`. Pick one,
write it down, never mix them.

**Transfers are not expenses.** Moving $500 from checking to savings is not $500
of spending. If you don't model this, the report is quietly wrong and you won't
notice for weeks.

**Category hierarchy or flat?** Flat is a simple list. Nested means recursive
queries and a parent field. Flat is fine for v1 — choose on purpose.

**Splits.** One Costco trip is part groceries, part household goods. One
category per transaction, or line items? Changes the schema significantly.

**Date, not datetime.** A transaction's date is a calendar date. A timestamp
means timezone conversion can move it into the previous month.

**Edit history.** Mutate in place, or append a correcting entry like real
accounting systems? v1 can mutate; know the tradeoff.

**Deleting a category.** Its transactions become uncategorised. Don't cascade a
delete through financial history.

---

## Working without AI

Make the rule specific, because a vague rule gets negotiated away at 11pm when
something won't compile.

**The rule:** no AI writing code, no AI debugging your errors, no AI explaining
your own code back to you. Docs, tutorials, Stack Overflow and books stay in.

**Write down what you expected before you go looking.** When something breaks,
type out: what I expected, what happened, what I've ruled out. Half the time you
solve it in the writing. That's the actual skill.

**Keep `DECISIONS.md` current.** Two minutes per entry. It's what you read in
six months when you've forgotten why amounts are integers, and it's what makes
you sound thoughtful rather than lucky in an interview.

Commit small and often, with messages that say why rather than what.
