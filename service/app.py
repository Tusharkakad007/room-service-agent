from fastapi import FastAPI
from pydantic import BaseModel
from service.agent import process_message
from service.db import guests_col
from datetime import datetime

app = FastAPI(title="Room Service Agent")

class Message(BaseModel):
    guest_id: str
    text: str

@app.post("/register")
async def register_guest(guest_id: str, preferences: str = ""):
    pref_list = [p.strip().lower() for p in preferences.split(",") if p.strip()]

    await guests_col.update_one(
        {"guest_id": guest_id},
        {
            "$set": {
                "guest_id": guest_id,
                "preferences": pref_list,
                "created_at": datetime.utcnow()
            }
        },
        upsert=True
    )

    return {"status": "guest registered", "guest_id": guest_id}

@app.post("/message")
async def message(payload: Message):
    response = await process_message(payload.guest_id, payload.text)
    return response
