from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/acesso', methods=['POST'])
def login():
    username = request.form['nome']
    email = request.form['email']
    password = request.form['senha']

    if username == 'mateus' and email == 'mateus@gmail.com' and password == '123':
        return redirect('/servicos')
    else:
        print('unknow user')
        return 'Usuario ou senha incorreta', 401

@app.route('/login')
def login_form():
    return render_template('login.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

if __name__ == '__main__':
    app.run(debug=True)