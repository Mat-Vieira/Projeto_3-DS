from flask import Blueprint, render_template, redirect, url_for

main_bp = Blueprint('main' , __name__)

noticias = [

    {
        'id': 'starfield',
        'titulo': 'Starfield',
        'descricao': 'Texto teste Texto teste Texto teste Texto teste Texto teste',
        'imagem': 'https://www.adrenaline.com.br/wp-content/uploads/2023/08/starfield-912x569.jpg',
        'fonte': ''
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
