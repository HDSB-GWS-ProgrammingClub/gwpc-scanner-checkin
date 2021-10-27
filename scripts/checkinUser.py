'''
This script writes the user's data into the Google Sheet
It is called from the Electron app code
'''

import sqlite3
import sys

# Initialize SQLite
db_connection = sqlite3.connect('data/data.db')
db_cursor = db_connection.cursor()



# Get data
studentID = sys.argv[1]
currentTime = sys.argv[2]

# Get user data
db_cursor.execute('''SELECT * FROM users
                    WHERE studentID=:studentID''',
    {'studentID': studentID}
)
user_tuple = db_cursor.fetchone()

# Parse data
user = {
    'name': user_tuple[0],
    'email': user_tuple[1],
    'phonenumber': user_tuple[2],
    'address': user_tuple[3],
    'studentID': user_tuple[4],
    'time': currentTime
}

# Check in
db_cursor.execute('''INSERT INTO checkedin
                    VALUES (:name, :email, :phonenumber, :address, :studentID, :time)''', user)
db_connection.commit()

print(user['name'])