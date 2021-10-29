from configdb import get_connection

def add_customer(name, status, mobile):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("INSERT INTO customer (name, status, mobile) VALUES (%s, %s, %s)",(name, status, mobile))
    myConnection.commit()
    myConnection.close()

def update_customer(name, status, mobile, id):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("UPDATE customer SET name=%s, status=%s, mobile=%s WHERE id=%s",(name, status, mobile, id))
    myConnection.commit()
    myConnection.close()

def delete_customer(id):
    myConnection = get_connection()
    with myConnection.cursor() as cursor:
        cursor.execute("DELETE from customer WHERE id=%s",(id))
    myConnection.commit()
    myConnection.close()

def get_customer():
    myConnection = get_connection()
    customers=[]
    with myConnection.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer")
        customers=cursor.fetchall()
    myConnection.close()
    return customers

def get_customer_id(id):
    myConnection=get_connection()
    customer=None
    with myConnection.cursor() as cursor:
        cursor.execute("SELECT id, name, status, mobile FROM customer WHERE id=%s",(id))
        customer=cursor.fetchone()
    myConnection.close()
    return customer

def check_if_invoices(id):
    myConnection=get_connection()
    invoice=None
    with myConnection.cursor() as cursor:
        cursor.execute("SELECT number, date, id, price, balance FROM invoice WHERE id=%s",(id))
        invoice=cursor.fetchall()
    myConnection.close()
    return invoice