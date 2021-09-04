import sqlite3

connection = sqlite3.connect('flask_tut.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        userName,
        passw,
        favoriteColor
    )VALUES(
        'Gordon',
        'Ramsay',
        'Black'
    );"""
)


cursor.execute(
    """INSERT INTO users(
        userName,
        passw,
        favoriteColor
    )VALUES(
        'IronMan',
        'Tony',
        'Gold'
    );"""
)

connection.commit()
cursor.close()
connection.close()