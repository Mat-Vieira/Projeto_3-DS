from flask import Blueprint, render_template, request, redirect, session, url_for
import secrets
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
    getuser = session.get('usuario')
    return render_template('servicos.html', nomeuser='Teste')
 
@usuario_bp.route('/acesso', methods=['POST'])
def acesso():
    username = request.form['login']
    password = request.form['password']


    if username in USERS and USERS[username] == password:
        session['usuario'] = username
        token = '1234'
        session['token'] = token
        return redirect(url_for('usuario.servicos'))
    else:
        session.pop('usuario', None)
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
    session['token'] = '1234'

    if login in USERS:
        logging.warning(f'Usuário já cadastrado: {login}')
        return "Usuário já cadastrado", 400

    USERS[login] = senha
    logging.info(f'Cadastro realizado com sucesso: {login}, {nome}')
    return redirect(url_for('usuario.servicos'))


@usuario_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('usuario.login'))


@usuario_bp.before_request
def check_auth():
    rotas_livres = [
        'usuario.login',
        'usuario.logout',
        'usuario.acesso',
        'usuario.cadastro',
        'usuario.add_cadastro'
    ]

    print("Endpoint acessado:", request.endpoint)  # Ajuda no debug

    if request.endpoint in rotas_livres:
        return

    token = session.get('token')
    if token:
        return

    return redirect(url_for('usuario.login'))