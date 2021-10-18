'''
This script creates a new user in the MongoDB database
It is called from the Electron app code
'''

import json
import sys

# Get data
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

# Parse data
with open('data/users.json', 'r') as f:
    users = json.load(f)

# Insert into JSON
users.append(data)
with open('data/users.json', 'w') as f:
    json.dump(users, f)

print('User created')