from logging import error
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='GET':
        return render_template('index.html',message='Aloha Aloha')
    else:
        username = request.form['username']
        password = request.form['password']
        if username=='paulo' and password=='123':
            return render_template('football.html', message='Login successful')
        else:
            error_message = 'Hint: The usual three numbers for paulo!'
            return render_template('index.html', message=error_message)

@app.route('/football', methods=['GET'])
def football():
    return render_template('football.html')

if __name__ == '__main__':
    app.run(port=7000, debug=True)



