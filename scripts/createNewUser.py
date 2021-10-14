'''
This script creates a new user in the MongoDB database
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

# Get data
data_list = list()
data_list.extend(sys.argv)
data_list.pop(0)

# Parse data
data = {
    'name': data_list[0],
    'email': data_list[1],
    'phonenumber': data_list[2],
    'address': data_list[3],
    'studentID': data_list[4],
}

# Insert user into  database
users_collection.insert_one(data)
print('User created')