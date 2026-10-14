# FastAPI Practice API

A small runnable API demonstrating route handlers, request validation with Pydantic, HTTP status codes, and basic CRUD-style reads/writes using temporary in-memory storage.

## Run locally

Requires Python 3.10 or newer.

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate

pip install -r requirements.txt
uvicorn app:app --reload
```

Open [the interactive API docs](http://127.0.0.1:8000/docs) after starting the server.

## Example

Create a student with `POST /students`:

```json
{
  "name": "Ayesha",
  "age": 20,
  "roll": 101
}
```

Then try `GET /students` or `GET /students/101`.

## Important limitations

- Records live only in memory and disappear when the server restarts.
- This is a learning example, not a production backend.
- There is no authentication or database persistence yet.
- `main.py` retains earlier commented practice notes; `app.py` is the runnable example.

## Next improvements

Add automated tests, persistent storage (SQLite/PostgreSQL), and validation for duplicate records at the database level.
