from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME", "todo_app")

client = AsyncIOMotorClient(MONGO_URI, server_api=ServerApi("1"))
db = client[DB_NAME]
task_collection = db['tasks']