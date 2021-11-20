import pymongo
import dotenv
import os
import sqlite3
import pymongo
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import subprocess

dotenv.load_dotenv()

# Initialize MongoDB
MONGODB_CONNECTION = os.getenv('MONGODB_URI')
mongodb_client = pymongo.MongoClient(MONGODB_CONNECTION)
db = mongodb_client['Cluster0']
users_collection = db['users']

# Config GSpread
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/spreadsheets','https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(f'{os.getcwd()}/creds.json', scope)
gspread_client = gspread.authorize(creds)
# checkin_sheet = gspread_client.open('GWPC Check-in 2.0').sheet1
checkin_sheet = gspread_client.open('GWPC Check-in 2.0 Test').sheet1

# Initialize SQLite
db_connection = sqlite3.connect('./data.db')
db_cursor = db_connection.cursor()



class Database:
    '''Methods to interact with database'''
    def pull_data():
        '''Pulls data from MongoDB and stores in SQLite'''

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
    
    def push_data():
        '''Pushes data to MongoDB/Google Sheet'''

        db_cursor.execute('SELECT * FROM users')
        users = db_cursor.fetchall()

        db_cursor.execute('SELECT * FROM checkedin')
        checkedin = db_cursor.fetchall()

        # Remove duplicate users
        new_users = []
        existing_users = [{k: v for k, v in d.items() if k != '_id'} for d in users_collection.find()]

        for i in users:
            user = {
                'name': i[0],
                'email': i[1],
                'phonenumber': i[2],
                'address': i[3],
                'studentID': i[4]
            }
            if user not in existing_users:
                new_users.append(user)

        if new_users:
            users_collection.insert_many(new_users)

        for i in checkedin:
            checkin_sheet.insert_row(i, 2)
    
    def shutdown():
        '''Delete SQLite file on close'''

        subprocess.call(['rm', 'data.db'])