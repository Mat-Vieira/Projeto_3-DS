from flask import Flask
from routes.main_routes import main_bp
from routes.usuario_route import usuario_bp

app = Flask(__name__)
app.secret_key = "yahoo"

app.register_blueprint(main_bp)
app.register_blueprint(usuario_bp)

if __name__ == '__name__':
    app.run(debug=True)

