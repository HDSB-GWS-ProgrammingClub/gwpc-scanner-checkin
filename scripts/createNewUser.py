'''
This script creates a new user in the MongoDB database
It is called from the Electron app code
'''

import sqlite3
import sys

# Initialize SQLite
db_connection = sqlite3.connect('data/data.db')
db_cursor = db_connection.cursor()



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

# Insert new user to local SQLite DB
db_cursor.execute('''INSERT INTO users
                    VALUES (:name, :email, :phonenumber, :address, :studentID)''', data)
db_connection.commit()

print('User created')