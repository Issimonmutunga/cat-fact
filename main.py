from fastapi import FastAPI, HTTPException
import httpx
from datetime import datetime, timezone

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "Welcome! Use /me to see my profile, time and cat fact."}


@app.get("/me")
async def profile_endpoint():
    url = "https://catfact.ninja/fact"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Failed to fetch cat fact")
        data = response.json()

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    return {
        "status": "success",
        "user": {
            "email": "besimonmutunga@gmail.com",
            "name": "Simon Mutunga",
            "stack": [
                "FastAPI",
                "Python",
                "HTTPX",
                "Uvicorn",
                "Railway",
                "GitHub"
            ],
        },
        "timestamp": now,
        "fact": data.get("fact"),
    }
