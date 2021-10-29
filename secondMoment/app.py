from datetime import date
from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect
import customer_controller
import invoice_controller
import pyautogui

app=Flask(__name__)

"""
Definición de rutas
"""
@app.route('/')
@app.route('/index')
def index():
    customers = customer_controller.get_customer()
    return render_template('index.html',customers=customers)

@app.route('/add_customer_form')
def add_customer_form():
    return render_template('add_customer.html')

@app.route('/add_customer',methods=['POST'])
def add_customer():
    name = request.form['name']
    status = request.form['status']
    mobile = request.form['mobile']
    customer_controller.add_customer(name,status,mobile)
    return redirect('/')

#Get the user to edit
@app.route('/edit_customer/<int:id>')
def edit_customer(id):
    customer = customer_controller.get_customer_id(id)
    return render_template('edit_customer.html',customer=customer)
#edit the data
@app.route('/update_customer',methods=['POST'])
def update_customer():
    #Get data from the invoked form
    id = request.form['id']
    name = request.form['name']
    status = request.form['status']
    mobile = request.form['mobile']
    customer_controller.update_customer(name,status,mobile,id)
    return redirect('/')

@app.route("/delete_customer", methods=["POST"])
def delete_customer():
    id = request.form['id']
    invoice = customer_controller.check_if_invoices(id)
    print(invoice)
    if(invoice):
        pyautogui.alert(text='You have pending invoices', title='ERROR', button='OK')
        print("You have pending invoices")
    else:
        customer_controller.delete_customer(id)
    return redirect('/index')


#---INVOICE---
@app.route('/invoice')
def invoice():
    invoices = invoice_controller.get_invoice()
    return render_template('invoice.html',invoices=invoices)

@app.route('/add_invoice_form')
def add_invoice_form():
    return render_template('add_invoice.html')

@app.route('/add_invoice',methods=['POST'])
def add_invoice():
    date = request.form['date']
    id = request.form['id']
    price = request.form['price']
    balance = request.form['balance']
    isvalidid = invoice_controller.check_customer_id(id)
    print(isvalidid)
    if(isvalidid):
        invoice_controller.add_invoice(date,id,price,balance)
    else:
        pyautogui.alert(text='The customer does not exist', title='ERROR', button='OK')
        print("The customer does not exist")
    return redirect('/invoice')

#Get the invoice to edit
@app.route('/edit_invoice/<int:number>')
def edit_invoice(number):
    invoice = invoice_controller.get_invoice_number(number)
    return render_template('edit_invoice.html',invoice=invoice)
#edit the data
@app.route('/update_invoice',methods=['POST'])
def update_invoice():
    #Get data from the invoked form
    number = request.form['number']
    date = request.form['date']
    price = request.form['price']
    balance = request.form['balance']
    invoice_controller.update_invoice(date,price,balance,number)
    return redirect('/invoice')

@app.route("/delete_invoice", methods=["POST"])
def delete_invoice():
    number = request.form['number']
    balance=invoice_controller.check_balance(number)
    print(balance[0])
    real_balance=balance[0]
    if(real_balance==0):
        invoice_controller.delete_invoice(number)
    else:
        pyautogui.alert(text='you must pay the remaining balance first', title='ERROR', button='OK')
        print("you must pay the remaining balance first")
    return redirect('/invoice')


# The server is running
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(port=5300, debug=True)