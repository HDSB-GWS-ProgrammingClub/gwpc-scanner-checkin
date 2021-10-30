'''
This script checks if a user exists in the MongoDB database
It is called from the Electron app code
'''

import sqlite3
import sys

# Initialize SQLite
db_connection = sqlite3.connect('./data.db')
db_cursor = db_connection.cursor()



# Get student ID
studentID = sys.argv[1]

# Find user
db_cursor.execute('''SELECT * FROM users
                    WHERE studentID=:studentID''',
    {'studentID': studentID}
)

# Print whether user exists
print(bool(db_cursor.fetchone()))