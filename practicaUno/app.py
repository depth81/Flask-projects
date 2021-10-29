from flask import Flask, render_template, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'bioturismo'
myConnection = MySQL(app) # vínculo entre la aplicación y la bd

#Rutas o endpoints
#Crear la ruta de inicio o home page
@app.route('/') # decorador para la ruta inicio
def index():
    nombres=['Paulo','Carlos','Juana','Carla','Patricia','Francisca']
    destinos=['NY','London','Tokyo','Paris','Moscow','Berlin']
    
    datosindex = {
        'titulo': 'Agencia de Viajes',
        'subtitulo': 'Bienvenido a nuestra agencia, estimado usuario! ',
        'nombres': nombres,
        'destinos': destinos,
        'cantUsuarios': len(nombres)
    }
    
    return render_template('index.html',data=datosindex)

@app.route('/makeplan')
def listPlan():
    ''' data = {}
    try:
        myCursor = myConnection.connection.cursor()
        sql = "SELECT id, nombre, costo FROM destino ORDER BY name"
        myCursor.execute(sql)
        names = myCursor.fetchall()
        data['message']='Success'
        print(names)
        data['names'] = names
    except Exception as ex:    
        data['mensaje'] = 'Error ...'
    return jsonify(data) '''
    return render_template('plan.html')

def notFound(error):
    #return render_template('notFound.html'),404
    return redirect(url_for('index'))

app.register_error_handler(404,notFound)

if __name__ == "__main__":
    app.run(port=7000, debug=True)

