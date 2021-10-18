'''
This script writes the user's data into the Google Sheet
It is called from the Electron app code
'''

import json
import sys

# Get data
studentID = sys.argv[1]
currentTime = sys.argv[2]

# Parse data
with open('data/users.json', 'r') as f:
    users = json.load(f)

with open('data/checkedin.json', 'r') as f:
    checkedin = json.load(f)

def getUser(studentID: str, json: dict):
    for i in json:
        if studentID == i['studentID']:
            return i

user = getUser(studentID, users)

info_list = list(i for i in user.values())
# Get date
info_list.append(currentTime)

# Insert into JSON
checkedin.append(info_list)
with open('data/checkedin.json', 'w') as f:
    json.dump(checkedin, f)

print(user['name'])