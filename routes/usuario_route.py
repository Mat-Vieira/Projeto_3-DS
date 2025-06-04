from flask import Blueprint, render_template, redirect, url_for, request, session

usuario_bp = Blueprint('usuario' , __name__)

@usuario_bp.route('/login')
def login_form():
    return render_template('login.html')

@usuario_bp.route('/acesso', methods=['POST'])
def login():
    username = request.form['nome']
    email = request.form['email']
    password = request.form['senha']

    if username == 'teste' and email == 'teste@gmail.com' and password == '123':
        return redirect('/servicos')
    else:
        print('unknow user')
        return 'Usuario ou senha incorreta', 401

@usuario_bp.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

