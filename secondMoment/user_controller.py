from configdb import get_connection

def add_user(name, email, password):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("INSERT INTO user (name, email, password) VALUES (%s, %s, %s)",(name, email, password))
    myConnection.commit()
    myConnection.close()

def update_user(name, email, password, id):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("UPDATE user SET name=%s, email=%s, password=%s WHERE id=%s",(name, email, password, id))
    myConnection.commit()
    myConnection.close()

def delete_user(id):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("DELETE from user WHERE id=%s",(id))
    myConnection.commit()
    myConnection.close()

def get_user():
    myConnection = get_connection()
    users=[]
    with myConnection.cursor() as cursor:
        cursor.execute("SELECT id, name, email, password FROM user")
        users=cursor.fetchall()
    myConnection.close()
    return users

def get_user_id(id):
    myConnection=get_connection()
    user=None
    with myConnection.cursor() as cursor:
        cursor.execute("SELECT id, name, email, password FROM user WHERE id=%s",(id))
        user=cursor.fetchone()
    myConnection.close()
    return user