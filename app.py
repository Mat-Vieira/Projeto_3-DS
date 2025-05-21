from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

noticias = [
    {
        'id': 'deadisland2',
        'titulo': 'Texto teste',
        'descricao': 'Texto teste',
        'imagem': 'https://assets.xboxservices.com/assets/1f/c8/1fc8ce3b-60b6-422a-84d3-16858472ccde.jpg?n=745632_GLP-Page-Hero-1084_1920x1080.jpg',
        'fonte': ''
    },
    {
        'id': 'vibrantvisuals',
        'titulo': 'Texto teste',
        'descricao': 'Texto teste',
        'imagem': 'https://pub-f354ec240bea480db7320bd0e29d972e.r2.dev/sites/8/2025/03/Minecraft_03_Vibrant_Visuals-dc564aedc997d04ebbf5.jpg',
        'fonte': ''
    },
    {
        'id': 'GTA6',
        'titulo': 'Texto teste',
        'descricao': 'Texto teste',
        'imagem': 'https://cdn.mos.cms.futurecdn.net/hBWx3UpU2Je2zJqrHLyUQW.jpg',
        'fonte': '',
    }
]


@app.route('/acesso', methods=['POST'])
def login():
    username = request.form['nome']
    email = request.form['email']
    password = request.form['senha']

    if username == 'teste' and email == 'teste@gmail.com' and password == '123':
        return redirect('/servicos')
    else:
        print('unknow user')
        return 'Usuario ou senha incorreta', 401

@app.route('/login')
def login_form():
    return render_template('login.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html', noticias=noticias)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/chat/<id>')
def chat(id):
    postagem = next((n for n in noticias if n['id'] == id), None)
    return render_template('chat.html', postagem=postagem)

if __name__ == '__main__':
    app.run(debug=True)