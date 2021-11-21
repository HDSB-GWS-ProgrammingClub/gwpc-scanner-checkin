import sqlite3
from datetime import datetime

# Initialize SQLite
db_connection = sqlite3.connect('./data.db')
db_cursor = db_connection.cursor()



class User:
    '''Methods to interact with users'''
    def check_user_exists(studentID: int):
        '''
        Check if user exists

        Returns: boolean
        '''

        # Find user
        db_cursor.execute('''SELECT * FROM users
                            WHERE studentID=:studentID''',
            {'studentID': studentID}
        )

        # Print whether user exists
        return bool(db_cursor.fetchone())
    
    def create_new_user(name, email, phonenumber, address, studentID):
        '''Create a new user'''

        data = {
            'name': name,
            'email': email,
            'phonenumber': phonenumber,
            'address': address,
            'studentID': studentID
        }

        # Insert new user to local SQLite DB
        db_cursor.execute('''INSERT INTO users
                            VALUES (:name, :email, :phonenumber, :address, :studentID)''', data)
        db_connection.commit()
    
    def checkin_user(studentID: int):
        '''
        Check-in user to the database

        Returns:
            - Tuple (user name, current time)
        '''

        current_time = str(datetime.now().strftime("%m/%d/%Y %I:%M:%S %p"))

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
            'time': current_time
        }

        # Check in
        db_cursor.execute('''INSERT INTO checkedin
                            VALUES (:name, :email, :phonenumber, :address, :studentID, :time)''', user)
        db_connection.commit()

        return (user_tuple[0], current_time)