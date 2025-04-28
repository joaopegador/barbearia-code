from flask import Flask
from flask_jwt_extended import JWTManager
from banco_dados.db import criar_tabelas
from routes.download_routes import download_bp

# Blueprints
from routes.user_routes import usuario_bp
from routes.servico_routes import servico_bp
from routes.agendamento_routes import agendamento_bp  # Adicionando a rota de agendamento

def create_app():
    app = Flask(__name__)

    # Configurações
    app.config.from_pyfile('config.py')

    # Inicializa JWT
    JWTManager(app)

    # Criação das tabelas
    criar_tabelas()

    # Registro dos Blueprints
    app.register_blueprint(usuario_bp, url_prefix='/usuarios')
    app.register_blueprint(servico_bp, url_prefix='/pedidos')
    app.register_blueprint(agendamento_bp, url_prefix='/agendamentos')  # Adicionando a rota de agendamentos
    app.register_blueprint(download_bp, url_prefix='/download')  # Adicionando a rota de downloads

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
