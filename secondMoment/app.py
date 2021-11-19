import os
from flask import Flask, render_template, url_for, flash, request, session
from werkzeug.utils import redirect
import customer_controller
import invoice_controller
import user_controller
import pyautogui
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#Configuring the file to store the files
app.config['UPLOAD_FOLDER'] = 'static/images'

@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    if request.method == "POST":
        # capture data from login.html
        email = request.form['email']
        password = request.form['password']
        # Create session variables
        session['email'] = email
        session['password'] = password
        #Validate the user input
        isValidUser = user_controller.login(session['email'],session['password'])
        if(isValidUser):
            return redirect(url_for('customer'))
        else:
            pyautogui.alert(text='The combination email/password does not exist', title='ERROR', button='ACCEPT')
            session.clear()
            return redirect('/index')

@app.route('/logout',methods=['GET','POST'])
def logout():
    #Delete session variables
    session.clear()
    return redirect(url_for('index'))

@app.route('/customer')
def customer():
    if "email" not in session:
        return redirect(url_for('index'))
    else:
        customers = customer_controller.get_customer()
        return render_template('customer.html',customers=customers)

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

#Get the customer to edit
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
    if "email" not in session:
        return redirect(url_for('index'))
    else:
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


#---USER---
@app.route('/user')
def user():
    if 'email' not in session:
        return redirect(url_for('index'))
    else:
        users = user_controller.get_user()
        return render_template('user.html',users=users)

@app.route('/add_user_form')
def add_user_form():
    return render_template('add_user.html')

@app.route('/add_user',methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    my_Data = request.files['ufilephoto']
    filename = secure_filename(my_Data.filename)
    my_Data.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    try:
        user_controller.add_user(name, email, password)
        pyautogui.alert(text='Successfully saved', title='MESSAGE', button='OK')
        return redirect('/user')
    except:
        pyautogui.alert(text='The email address already exists', title='ERROR', button='OK')
        return redirect(url_for('add_user_form'))

#Get the user to edit
@app.route('/edit_user/<int:id>')
def edit_user(id):
    user = user_controller.get_user_id(id)
    return render_template('edit_user.html',user=user)
#edit the data
@app.route('/update_user',methods=['POST'])
def update_user():
    #Get data from the invoked form
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    id = request.form['id']
    my_Data = request.files['ufilephoto']
    filename = secure_filename(my_Data.filename)
    my_Data.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
    user_controller.update_user(name,email,password,id)
    pyautogui.alert(text='Successfully edited!', title='MESSAGE', button='OK')
    """ flash('The file has been uploaded') """
    return redirect('/user')
    
@app.route("/delete_user", methods=["POST"])
def delete_user():
    id = request.form['id']
    user_controller.delete_user(id)
    return redirect('/user')


# The server is running
if __name__ == "__main__":
    app.run(port=5300, debug=True)