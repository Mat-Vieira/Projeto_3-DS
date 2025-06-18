from flask import Blueprint, render_template, request, redirect, session, url_for
import logging

logging.basicConfig(level=logging.INFO)

usuario_bp = Blueprint('usuario', __name__)

USERS = { 
    "teste@": "123"
}

@usuario_bp.route('/login')
def login():
    return render_template('login.html')

@usuario_bp.route('/servicos')
def servicos():
    #getuser = session.get('usuario')
    return render_template('servicos.html', nomeuser='Teste')

@usuario_bp.route('/acesso', methods=['POST'])
def acesso():
    username = request.form['login']
    password = request.form['password']


    if username in USERS and USERS[username] == password:
        session['usuario'] = username
        return redirect(url_for('usuario.servicos'))
    else:
        logging.warning(f'Usuário ou senha incorretos: {username}')
        session.pop('usuario', None)
        print('Usuário não encontrado')
        return "Usuário ou senha incorretos", 401

@usuario_bp.route('/cadastro')
def cadastro():

    return render_template('cadastro.html')

@usuario_bp.route('/add_cadastro', methods=['POST'])
def add_cadastro():
    login = request.form['login']
    senha = request.form['senha']
    nome = request.form['nome']


    session['usuario'] = {
        'login': login,
        'nome': nome,
    }

    if login in USERS:
        logging.warning(f'Usuário já cadastrado: {login}')
        return "Usuário já cadastrado", 400

    USERS[login] = senha
    logging.info(f'Cadastro realizado com sucesso: {login}, {nome}')
    return redirect(url_for('usuario.servicos'))


@usuario_bp.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('/'))