'''
Writes new JSON data to MongoDB
Called when Electron app is closed or when button pressed
'''

import pymongo
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import dotenv
import os
import json
import dotenv

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
checkin_sheet = gspread_client.open('GWPC Check-in 2.0').sheet1

with open('data/users.json', 'r') as f:
    users = json.load(f)

with open('data/checkedin.json', 'r') as f:
    checkedin = json.load(f)

# Remove duplicate users
new_users = []
existing_users = [{k: v for k, v in d.items() if k != '_id'} for d in users_collection.find()]

for i in users:
    if i not in existing_users:
        new_users.append(i)

if new_users:
    users_collection.insert_many(new_users)

for i in checkedin:
    checkin_sheet.insert_row(i, 2)