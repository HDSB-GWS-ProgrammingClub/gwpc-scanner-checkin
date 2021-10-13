'''
This script checks if a user exists in the MongoDB database
It is called from the Electron app code
'''

import pymongo
import dotenv
import os
import sys

dotenv.load_dotenv()

# Initialize MongoDB
MONGODB_CONNECTION = os.getenv('MONGODB_URI')
mongodb_client = pymongo.MongoClient(MONGODB_CONNECTION)
db = mongodb_client['Cluster0']
users_collection = db['users']

studentID = sys.argv[1]

# Check if user exists
if (users_collection.find_one({'studentID': studentID})):
    print('true')
else:
    print('false')