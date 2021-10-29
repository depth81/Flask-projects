from flask import Flask, render_template, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bdhelloworldflask'
myConnection = MySQL(app) # vínculo entre la aplicación y la bd

#Rutas o endpoints
#Crear la ruta de inicio o home page
@app.route('/') # decorador para la ruta inicio
def index():
    #return '<h1>Hola mundo desde Flask 3</h1>'
    vehiculos=['Mazda','Renault','Toyota','Chevrolet','Audi','Lamborghini']
    precios=[30000,20000,25000,20000,50000,200000]
    
    datosindex = {
        'titulo': 'sistema de prueba',
        'subtitulo': 'Bienvenido al sistema, estimado usuario: ',
        'usuario': 'myTestUser',
        'referencias': ['3','Logan','Celica','Aveo','A5','Countach'],
        'vehiculos': vehiculos,
        'precios': precios,
        'cantVehiculos': len(vehiculos)
    }
    
    return render_template('index.html',data=datosindex)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cars')
def listCars():
    data = {}
    try:
        myCursor = myConnection.connection.cursor()
        sql = "SELECT id, brand, model, price FROM car ORDER BY brand"
        myCursor.execute(sql)
        cars = myCursor.fetchall()
        data['message']='Success'
        print(cars)
        data['cars'] = cars
    except Exception as ex:    
        data['mensaje'] = 'Error ...'
    return jsonify(data) # recordar importar jsonify

def notFound(error):
    #return render_template('notFound.html'),404
    return redirect(url_for('index'))

app.register_error_handler(404,notFound)

if __name__ == "__main__":
    app.run(port=7000, debug=True)

