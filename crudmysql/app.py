from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect
import user_controller

app=Flask(__name__)

"""
Definición de rutas
"""
@app.route('/')
@app.route('/index')
def index():
    users = user_controller.get_user()
    return render_template('index.html',users=users)

@app.route('/add_user_form')
def add_user_form():
    return render_template('add_user.html')

@app.route('/add_user',methods=['POST'])
def add_user():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    user_controller.add_user(name,email,phone,password)
    return redirect('/')

#Get the user to edit
@app.route('/edit_user/<int:id>')
def edit_user(id):
    user = user_controller.get_user_id(id)
    return render_template('edit_user.html',user=user)
#edit the data
@app.route('/update_user',methods=['POST'])
def update_user():
    #Get data from the invoked form
    id = request.form['id']
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']
    user_controller.update_user(name,email,phone,password,id)
    return redirect('/')

@app.route("/delete_user", methods=["POST"])
def delete_user():
    user_controller.deleter_user(request.form['id'])
    return redirect('/index')

# The server is running
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8000, debug=True)
    app.run(port=5300, debug=True)