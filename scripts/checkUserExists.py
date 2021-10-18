'''
This script checks if a user exists in the MongoDB database
It is called from the Electron app code
'''

import sys
import json

studentID = sys.argv[1]

with open('data/users.json', 'r') as f:
    users = json.load(f)

def find_user(users: dict):
    for user in users:
        if user['studentID'] == studentID:
            return 'true'
    return 'false'

print(find_user(users))