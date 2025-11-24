from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "room_service_db")

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

menu_col = db["menu"]
guests_col = db["guests"]
convos_col = db["conversations"]
