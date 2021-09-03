import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(

    """CREATE TABLE users(
        pk INTEGER PRIMARY KEY AUTOINCREMENT,
        userName VARCHAR(16),
        passw VARCHAR(32),
        favoriteColor VARCHAR(32)
    );"""

)