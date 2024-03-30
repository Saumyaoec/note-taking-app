from motor.motor_asyncio import AsyncIOMotorClient
import os

# Fetch MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DATABASE_NAME = "note_db"

# Establish connection to MongoDB
try:
    client = AsyncIOMotorClient(MONGO_URI)
    database = client[DATABASE_NAME]
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    # Handle the error appropriately, e.g., raise an exception or exit the application

# Define MongoDB collections
users_collection = database["users"]
notes_collection = database["notes"]
