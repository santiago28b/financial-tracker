# Decisions

One entry per real design choice. What I picked, what else I considered, why.
Two minutes each. Future me will thank present me.

Format:

```
## NNN — Title
Date:
Status: open | decided
Decision:
Alternatives considered:
Why:
```

---

## 001 — How to store money amounts

Date:
Status: open

The question: floats are broken for money (`0.1 + 0.2 != 0.3`). Integer cents,
or Python `Decimal` with Postgres `Numeric`?

Alternatives: integer cents / Decimal+Numeric / float (no)

Decision:

Why:

---

## 002 — How transfers are modelled

Date:
Status: open

Moving $500 from checking to savings is not $500 of spending. If this isn't
modelled, the "where did my money go" report is quietly wrong.

Alternatives: a transaction type flag / two linked transactions netting to zero
/ a separate transfers table

Decision:

Why:

---

## 003 — Category hierarchy: flat or nested

Date:
Status: open

Flat is a simple list. Nested (Food → Groceries / Restaurants) means a parent
field and recursive queries.

Decision:

Why:

---

## 004 — Transaction splits

Date:
Status: open

One Costco trip is part groceries, part household goods. One category per
transaction, or a set of line items each with their own?

Note: changes the schema significantly, so decide now even if v2 builds it.

Decision:

Why:

---

## 005 — Date vs datetime for a transaction

Date:
Status: open

A transaction's date is a calendar date. Storing a timestamp means timezone
conversion can move a transaction into the previous month.

Decision:

Why:

---

## 006 — Edit history

Date:
Status: open

When a transaction's amount is corrected, does the old value disappear?
Mutate in place, or append a correcting entry like real accounting systems?

Decision:

Why:

---

## 007 — What happens when a category is deleted

Date:
Status: open

Its transactions vanish, or become uncategorised?

Decision:

Why:

---

## 008 — Supabase for database and auth, not for the frontend

Date: 2026-09-22
Status: decided

Decision: Supabase as hosted Postgres + auth provider, sitting *behind* my own
FastAPI. React talks to my API; my API talks to Supabase. Not using Supabase as
the whole backend, and not using it from the frontend directly.

Alternatives considered:

- Supabase as the entire backend (React → Supabase, RLS for authorization, no
  FastAPI). Faster to build, production-viable, but skips the backend entirely.
- Self-hosted Postgres in Docker + hand-rolled auth. Most learning, but auth is
  a lot of security surface area to get wrong on an app holding real financial
  data that other people might eventually use.

Why:

- Keeps every learning goal (backend, API design, React, JWT verification) and
  drops the two parts that are pure setup tax.
- Auth is the one piece worth handing to a provider here. I still write the JWT
  verification middleware myself, which is the part that teaches me how it works
  and where the real bug lives.
- Supabase is just Postgres, so SQLAlchemy and Alembic are unaffected.

Consequences / follow-ups:

- Alembic needs the *direct* connection string, not the pooled one.
- Turn on row-level security anyway, as defense in depth.
- Free tier pauses after ~1 week of no database activity — schedule a ping or
  pay before the URL goes on a résumé.
- Not learning bcrypt / session design / token refresh. Accepted; possible
  throwaway weekend project later to fill the gap.
