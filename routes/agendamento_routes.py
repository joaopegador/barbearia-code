from flask import Blueprint, request, jsonify
from controllers.agendamento_controller import criar_agendamento_controller, listar_agendamentos_usuario_controller

agendamento_bp = Blueprint('agendamento', __name__)

@agendamento_bp.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    data = request.get_json()

    usuario_id = data.get('usuario_id')
    barbeiro_id = data.get('barbeiro_id')
    servico_id = data.get('servico_id')
    data_agendamento = data.get('data')
    hora = data.get('hora')

    if not all([usuario_id, barbeiro_id, servico_id, data_agendamento, hora]):
        return jsonify({"erro": "Todos os campos são obrigatórios."}), 400

    resposta, status_code = criar_agendamento_controller(usuario_id, barbeiro_id, servico_id, data_agendamento, hora)
    return jsonify(resposta), status_code

@agendamento_bp.route('/agendamentos/<int:usuario_id>', methods=['GET'])
def listar_agendamentos(usuario_id):
    resposta, status_code = listar_agendamentos_usuario_controller(usuario_id)
    return jsonify(resposta), status_code
