#Handling the OS
import os

from flask import Flask, render_template, redirect, request, flash
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#Configuring the file to store the files
app.config['UPLOAD_FOLDER'] = 'static/images'

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        my_Data = request.files['ufile']
        filename = secure_filename(my_Data.filename)
        my_Data.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        flash('The file has been uploaded')
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=4500)