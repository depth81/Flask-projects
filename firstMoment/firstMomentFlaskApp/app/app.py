from flask import Flask, render_template

app = Flask(__name__)

#Rutas o endpoints
#Crear la ruta de inicio o home page
@app.route('/') # decorador para la ruta inicio
def index():
    instrumentosMusicales=['Guitarra','Percusión','Bajo','Voz']
    
    datosindex = {
        'Banda': 'Wormkult',
        'canción': 'TheEdgeOfInfamy',
        'autores': ['Paulo','Óscar','Diego','Harold'],
        'instrumentos': instrumentosMusicales,
        'cantInstrumentos': len(instrumentosMusicales)
    }
    
    return render_template('index.html',data=datosindex)

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(port=7000, debug=True)