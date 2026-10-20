# Solo reps

A solo rep is a short exam you take alone. It shows what you can build without help.

## The rules

- **Time:** 60 minutes, with a timer. Stop when it rings, whether you've finished or not.
- **Where:** a new empty folder *outside* this repo, e.g. `~/projects/solo-reps/s2r-grades/`.
- **Allowed:** official docs, Google, Stack Overflow, your own past code in this repo.
- **Not allowed:** Claude, ChatGPT, Copilot, or any AI autocomplete. Turn off the IDE's AI suggestions.
- **Start with the ritual:** 3 lines of plain English → signature → one failing test.
  Same as every session.
- **Stuck?** Write expected / actual / ruled out in a `STUCK.md` in that folder,
  then keep going. That file is gold for the debrief.

**Done** means 60 minutes are up and the debrief is written. Finishing the build isn't required.

## The debrief (5 min, right after)

Open `/session` and answer these. Claude copies the answers into the solo rep log in `LEARNER.md`.

1. How far did I get? (which requirements work)
2. Where did I get stuck first, and for how long?
3. What did I have to look up?
4. What would I do differently next time?

---

## S2.R — Grades module (after Stage 2)

Pure Python + pytest. No web, no database.

1. A `Grade` type with a subject name and a score from 0 to 100. Creating one with
   a score outside that range raises an error.
2. `average(grades)` returns the average score. Decide what happens with an empty list, and test it.
3. `letter(score)` returns A (90+), B (80+), C (70+), D (60+) or F.
4. Tests: at least one per function, plus the edges (exactly 90, exactly 0, an empty list).

Stretch: `best_subject(grades)`.

## S3.R — Library schema (after Stage 3)

SQL only, in a fresh SQLite file (`sqlite3 library.db`) or a scratch Supabase schema.

1. Tables for `books`, `members` and `loans`. Each has a primary key; `loans` has
   foreign keys to the other two.
2. Constraints: a book's title is required; a loan's due date can't be before its start date.
3. Insert 3 books, 2 members, 4 loans. Then try one bad insert and watch it fail.
4. One query: how many loans each member has, most first.

Stretch: a query for overdue loans.

## S4.R — Bookmarks API (after Stage 4)

FastAPI. Keep data in a Python list in memory, with no database.

1. `POST /bookmarks` with a `url` and `title` → returns the created bookmark with an id, status 201.
2. `GET /bookmarks` → the list.
3. `DELETE /bookmarks/{id}` → 204, and 404 if it doesn't exist.
4. One test with `TestClient` that creates a bookmark and then lists it.

Stretch: reject a `url` that doesn't start with `http`, with a 422.

## S6.R — Bookmarks with auth (after Stage 6)

Start from your S4.R code (copy the folder).

1. A dependency that reads an `Authorization: Bearer <token>` header and rejects a
   missing or wrong token with 401. A hard-coded dict of `token → user_id` is fine.
2. Each bookmark stores the user_id of whoever created it, taken from the token,
   never from the body.
3. `GET /bookmarks` returns only the caller's bookmarks.
4. A test proves user A can't delete user B's bookmark.

Stretch: real JWTs with `pyjwt` and a shared secret.

## S8.R — Movie genre tagger (after Stage 8)

Python script + the Anthropic SDK. The API key comes from the environment.

1. A list of 10 movie titles in the code.
2. Send them to the LLM; get back JSON in the shape `[{"title": ..., "genre": ...}]`.
3. Validate the reply with Pydantic. A malformed reply is caught and reported, not a crash.
4. Print the results and the total tokens used.

Stretch: 5 titles with a known genre, and print the accuracy.
