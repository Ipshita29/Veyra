import os

from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

# MongoClient connects lazily, so importing this module never fails offline.
client = MongoClient(os.getenv("MONGODB_URI", "mongodb://localhost:27017"))
db = client[os.getenv("MONGODB_DB", "veyra")]
