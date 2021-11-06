from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key='jdsdisoj432$%'

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    if request.method == "POST":
        # capturar datos enviados por el templates login.html
        email = request.form['email']
        password = request.form['password']
        rol = request.form['rol']
        # creación de variables de sesión
        session['email'] = email
        session['password'] = password
        session['rol'] = rol
        return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    if session['email'] == 'xx@gmail.com' and session['password'] == '11' and session['rol'] == 'admin':
        return render_template('cart.html')
    else:
        #return "No tiene permiso para acceder a este recurso ..."
        return redirect('/')

@app.route('/logout',methods=['POST'])
def logout():
    #borrar el contenido de las variables de sesión
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=2300)