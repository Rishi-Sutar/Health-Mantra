from pymongo import MongoClient
from django.conf import settings

# Create a MongoDB connection
client = MongoClient(settings.MONGO_DB_URI)
db = client[settings.MONGO_DB_NAME]
