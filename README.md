# Uptime Monitor

A service that checks the availability of websites and services and keeps a history of the results.

> Work in progress.

## Stack

- Python 3
- FastAPI
- Uvicorn

## Run locally

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Then open:

- http://127.0.0.1:8000/health — service health check
- http://127.0.0.1:8000/docs — interactive API docs (Swagger)

## Roadmap

- [ ] Store check targets in PostgreSQL
- [ ] Periodic HTTP and TCP checks
- [ ] Check history and uptime percentage
- [ ] Tests (pytest)
- [ ] Docker Compose setup