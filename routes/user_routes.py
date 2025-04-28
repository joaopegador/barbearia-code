from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from controllers.user_controller import UsuarioControlador

usuario_bp = Blueprint('usuarios', __name__)

# Rota para registrar um novo usuário
@usuario_bp.route('/registrar', methods=['POST'])
def registrar_usuario():
    dados = request.get_json()
    resultado, status_code = UsuarioControlador.registrar_usuario(dados)
    return jsonify(resultado), status_code

# Rota para fazer login do usuário
@usuario_bp.route('/login', methods=['POST'])
def logar_usuario():
    dados = request.get_json()
    resultado, status_code = UsuarioControlador.logar_usuario(dados)
    return jsonify(resultado), status_code
