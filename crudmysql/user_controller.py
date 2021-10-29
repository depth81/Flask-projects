from configdb import get_connection

def add_user(name, email, phone, password):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("INSERT INTO users (name, email, phone, password) VALUES (%s, %s, %s, %s)",(name, email, phone, password))
    myConnection.commit()
    myConnection.close()

def update_user(name, email, phone, password, id):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("UPDATE users SET name=%s, email=%s, phone=%s, password=%s WHERE id=%s",(name, email, phone, password, id))
    myConnection.commit()
    myConnection.close()

def deleter_user(id):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("DELETE from users WHERE id=%s",(id))
    myConnection.commit()
    myConnection.close()

def get_user():
    myConnection = get_connection()
    users=[]
    with myConnection.cursor() as cursor:
        cursor.execute("SELECT id, name, email, phone, password FROM users")
        users=cursor.fetchall()
    myConnection.close()
    return users

def get_user_id(id):
    myConnection=get_connection()
    user=None
    with myConnection.cursor() as cursor:
        cursor.execute("SELECT id, name, email, phone, password FROM users WHERE id=%s",(id))
        user=cursor.fetchone()
    myConnection.close()
    return user
