from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/time")
def get_time():
    now = datetime.now(timezone.utc)
    return {"server_time": now.isoformat()}
