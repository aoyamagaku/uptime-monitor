from fastapi import FastAPI

app = FastAPI(title="Uptime Monitor")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {
        "name": "Uptime Monitor",
        "version": "0.1.0",
    }
