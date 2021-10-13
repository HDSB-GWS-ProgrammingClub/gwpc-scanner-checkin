'''
This script writes the user's data into the Google Sheet
It is called from the Electron app code
'''

import pymongo
import dotenv
import os
import sys
import gspread
from oauth2client.service_account import ServiceAccountCredentials

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

# Get data
studentID = sys.argv[1]
currentTime = sys.argv[2]

# Parse data
user = users_collection.find_one({'studentID': studentID})
del user['_id']
info_list = list(i for i in user.values())
# Get date
info_list.append(currentTime)

# Insert into Google Sheet
checkin_sheet.insert_row(info_list, 2)

print(user['name'])