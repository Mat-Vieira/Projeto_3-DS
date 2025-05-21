from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#@app.route('/')
#def index():
 #   return render_template('index.html')

noticias = [
    
    {
        'id': 'deadisland2',
        'titulo': 'Dead Island 2 de graça na Epic Games Store',
        'descricao': 'Texto teste',
        'imagem': 'https://www.adrenaline.com.br/wp-content/uploads/2023/04/dead-island-2-912x569.jpg',
        'fonte': ''
    },
    {
        'id': 'vibrantvisuals',
        'titulo': 'Vibrant Visuals implementado no Minecraft via Experimento',
        'descricao': 'Texto teste',
        'imagem': 'https://pub-f354ec240bea480db7320bd0e29d972e.r2.dev/sites/8/2025/03/Minecraft_03_Vibrant_Visuals-dc564aedc997d04ebbf5.jpg',
        'fonte': ''
    },
    {
        'id': 'GTA6',
        'titulo': 'GTA 6 pode ser adiado antes de 26 de Maio?',
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

@app.route('/')
def servicos():
    return render_template('servicos.html', noticias=noticias)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/chat/<chat_id>')
def chat(chat_id):
    noticia = next((n for n in noticias if n['id'] == chat_id), None)
    if not noticia:
        return redirect(url_for('servicos'))
    return render_template('chat.html', noticias=noticias, noticia=noticia)

if __name__ == '__main__':
    app.run(debug=True)
