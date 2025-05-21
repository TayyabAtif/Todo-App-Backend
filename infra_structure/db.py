from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://fastapi_user:your_secure_password@cluster0.okp6zaq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
client = AsyncIOMotorClient(MONGO_URI)
db = client["fastapi_db"]  # You can name your DB anything
