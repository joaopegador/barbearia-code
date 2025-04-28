# routes/upload_routes.py

from flask import Blueprint, request, jsonify
from controllers.upload_controller import UploadController

upload_bp = Blueprint('upload_bp', __name__)

# Enviar arquivo
@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    return UploadController.upload_file()

# Listar arquivos
@upload_bp.route('/upload', methods=['GET'])
def listar_arquivos():
    return UploadController.listar_arquivos()

# Deletar arquivo
@upload_bp.route('/upload/<nome_arquivo>', methods=['DELETE'])
def deletar_arquivo(nome_arquivo):
    return UploadController.deletar_arquivo(nome_arquivo)

# Atualizar arquivo (se você tiver implementado atualizar)
@upload_bp.route('/upload/<nome_arquivo>', methods=['PUT'])
def atualizar_arquivo(nome_arquivo):
    return UploadController.atualizar_arquivo(nome_arquivo)
