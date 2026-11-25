from fastapi import FastAPI, HTTPException
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db import engine

app = FastAPI(title="Uptime Monitor")


@app.get("/health")
def health():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except SQLAlchemyError:
        raise HTTPException(
            status_code=503,
            detail="Database connection failed")

    return {"status": "ok", "database": "ok"}


@app.get("/")
def root():
    return {
        "name": "Uptime Monitor",
        "version": "0.1.0",
    }
