from flask import Blueprint, jsonify
from controllers.servico_controller import listar_servicos_controller

servico_bp = Blueprint('servico', __name__)

@servico_bp.route('/servicos', methods=['GET'])
def listar_servicos():
    resposta, status_code = listar_servicos_controller()
    return jsonify(resposta), status_code
