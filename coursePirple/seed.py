import sqlite3
import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread=False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        favorite_color
    )VALUES(
        'paulo',
        '123',
        'Blue'
    );"""
)

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        favorite_color
    )VALUES(
        'ana',
        '123',
        'Green'
    );"""
)

connection.commit()
cursor.close()
connection.close()

