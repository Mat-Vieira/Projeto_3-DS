from flask import Blueprint, render_template, redirect, url_for

main_bp = Blueprint('main' , __name__)

noticias = [

    {
        'id': 'starfield',
        'titulo': 'Starfield',
        'descricao': 'Texto teste',
        'imagem': 'https://www.adrenaline.com.br/wp-content/uploads/2023/08/starfield-912x569.jpg',
        'fonte': ''
    },
    {
        'id': 'deadisland2',
        'titulo': 'Dead Island 2',
        'descricao': 'Texto teste',
        'imagem': 'https://www.adrenaline.com.br/wp-content/uploads/2023/04/dead-island-2-912x569.jpg',
        'fonte': ''
    },
    {
        'id': 'vibrantvisuals',
        'titulo': 'Minecraft',
        'descricao': 'Texto teste',
        'imagem': 'https://pub-f354ec240bea480db7320bd0e29d972e.r2.dev/sites/8/2025/03/Minecraft_03_Vibrant_Visuals-dc564aedc997d04ebbf5.jpg',
        'fonte': ''
    },
    {
        'id': 'GTA6',
        'titulo': 'GTA 6',
        'descricao': 'Texto teste',
        'imagem': 'https://cdn.mos.cms.futurecdn.net/hBWx3UpU2Je2zJqrHLyUQW.jpg',
        'fonte': '',
    }
]


@main_bp.route('/')
def login_form():
    return render_template('index.html')

@main_bp.route('/servicos')
def servicos():
    return render_template('servicos.html', noticias=noticias)

@main_bp.route('/chat/<chat_id>')
def chat(chat_id):
    noticia = next((n for n in noticias if n['id'] == chat_id), None)
    if not noticia:
        return redirect(url_for('servicos'))
    return render_template('chat.html', noticias=noticias, noticia=noticia)

if __name__ == '__main__':
   main_bp.run(debug=True)
