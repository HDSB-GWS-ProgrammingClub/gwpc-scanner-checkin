'''
Writes MongoDB data to JSON
Called when Electron app is run
'''

import pymongo
import dotenv
import os
import json

dotenv.load_dotenv()

# Initialize MongoDB
MONGODB_CONNECTION = os.getenv('MONGODB_URI')
mongodb_client = pymongo.MongoClient(MONGODB_CONNECTION)
db = mongodb_client['Cluster0']
users_collection = db['users']

users = [{k: v for k, v in d.items() if k != '_id'} for d in users_collection.find()]

with open('data/users.json', 'w') as f:
    json.dump(users, f)

with open('data/checkedin.json', 'w') as f:
    json.dump([], f)