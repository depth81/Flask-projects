from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html', message='Aloha!, Aloha!')
    else:
        userName = request.form['userName']
        password = request.form['password']
        if userName == 'Gordon' and password == 'Ramsay':
            return render_template('football.html', message = 'Loggedin succesfully')
        else:
            error_message = 'Hint: He curses a lot.'
            """ return render_template('index.html', message=error_message) """
            return render_template('index.html', message=error_message)


@app.route('/football', methods=['GET','POST'])
def football():
    return render_template('football.html')

if __name__ == '__main__':
    app.run(port=7000, debug=True)



