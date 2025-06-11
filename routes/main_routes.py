from flask import Blueprint, render_template, redirect, url_for

main_bp = Blueprint('main' , __name__)

noticias = [
    {   'id': 'xbox-portatil',
        'titulo': 'Xbox AlyX Portatil',
        'descricao': 'Texto teste Texto teste Texto teste Texto teste Texto teste',
        'imagem': 'https://s2-techtudo.glbimg.com/-rRtUzW0CSfa0jn7giiVyISvWUU=/0x0:1200x675/984x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2025/X/f/rna6fkSYqrtHCLXy1auA/rog-xbox-ally-portatil-microsoft-this-is-an-xbox.jpg',
        'fonte': ''
    },
    {   'id': 'switch-2',
        'titulo': 'Nintendo Switch 2',
        'descricao': 'Texto teste Texto teste Texto teste Texto teste Texto teste',
        'imagem': 'https://files.tecnoblog.net/wp-content/uploads/2025/01/nintendo-switch-2-capa-1060x596.jpg',
        'fonte': ''
    },
    {   'id': 'RE-9',
        'titulo': 'Resident Evil 9 Requiem',
        'descricao': 'Texto teste Texto teste Texto teste Texto teste Texto teste',
        'imagem': 'https://viciados.net/wp-content/uploads/2025/06/Resident-Evil-Requiem-9-Summer-Game-Fest-2025-Capcom-1280x720.webp',
        'fonte': ''
    },
    {   'id': 'minecraft',
        'titulo': 'Minecraft',
        'descricao': 'Texto teste Texto teste Texto teste Texto teste Texto teste',
        'imagem': 'https://xboxwire.thesourcemediaassets.com/sites/8/2024/05/Hero-bdef2532984d6fcafc40.jpg',
        'fonte': ''
    },
    {   'id': 'Playstation-5',
        'titulo': 'Playstation 5',
        'descricao': 'Texto teste Texto teste Texto teste Texto teste Texto teste',
        'imagem': 'https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUyYmFzN282ZTN2MG85NHZkMDd6eXkxMnN6bHhjcTlocDlob3pjamhwbyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/dKTJvjV16COKNAhLJV/giphy-downsized-large.gif',
        'fonte': ''
    },
    {   'id': 'red-dead-redemption-2',
        'titulo': 'Red Dead Redemption 2',
        'descricao': 'Texto teste Texto teste Texto teste Texto teste Texto teste',
        'imagem': 'https://sm.ign.com/ign_br/screenshot/default/blob_p47c.jpg',
        'fonte': ''
    },
    {   'id': 'gta6',
        'titulo': 'GTA 6',
        'descricao': 'Texto teste Texto teste Texto teste Texto teste Texto teste',
        'imagem': 'https://cdn.oantagonista.com/uploads/2025/05/gta-6-1024x576.webp',
        'fonte': ''
    },
    {
        'id': 'starfield',
        'titulo': 'Starfield',
        'descricao': 'Texto teste Texto teste Texto teste Texto teste Texto teste',
        'imagem': 'https://www.adrenaline.com.br/wp-content/uploads/2023/08/starfield-912x569.jpg',
        'fonte': ''
    }
]

@main_bp.app_context_processor
def inject_noticias():
    return dict(noticias=noticias)

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
        return redirect(url_for('main_bp.servicos'))
    return render_template('chat.html', noticias=noticias, noticia=noticia)

if __name__ == '__main__':
   main_bp.run(debug=True)
