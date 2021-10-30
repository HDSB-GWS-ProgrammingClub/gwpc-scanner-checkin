'''
Writes MongoDB data to SQLite
Called when Electron app is run
'''

import pymongo
import dotenv
import os
import sqlite3

dotenv.load_dotenv()

# Initialize MongoDB
MONGODB_CONNECTION = os.getenv('MONGODB_URI')
mongodb_client = pymongo.MongoClient(MONGODB_CONNECTION)
db = mongodb_client['Cluster0']
users_collection = db['users']

# Initialize SQLite
db_connection = sqlite3.connect('./data.db')
db_cursor = db_connection.cursor()



# Get all users from MongoDB
users = []
users.extend(users_collection.find())

# Clear tables
db_cursor.execute('DROP TABLE IF EXISTS users')
db_cursor.execute('DROP TABLE IF EXISTS checkedin')

# Create tables
db_cursor.execute('''CREATE TABLE users
                    (name TEXT, email TEXT, phonenumber TEXT, address TEXT, studentID TEXT)''')
db_cursor.execute('''CREATE TABLE checkedin
                    (name TEXT, email TEXT, phonenumber TEXT, address TEXT, studentID TEXT, time TEXT)''')

# Write users to local SQLite DB
for user in users:
    db_cursor.execute('''INSERT INTO users
                        VALUES (:name, :email, :phonenumber, :address, :studentID)''',
        {
            'name': user['name'],
            'email': user['email'],
            'phonenumber': user['phonenumber'],
            'address': user['address'],
            'studentID': user['studentID']
        }
    )
db_connection.commit()