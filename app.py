from flask import Flask
from routes.main_routes import main_bp
from routes.usuario_route import usuario_bp

app = Flask(__name__)
app.secret_key = "yahoo"

app.register_blueprint(main_bp)
app.register_blueprint(usuario_bp, url_prefix='/usuario')

if __name__ == '__main__':
    print("Iniciando servidor Flask...")
    app.run(debug=True)


