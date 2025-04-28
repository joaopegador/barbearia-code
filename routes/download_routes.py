from flask import Blueprint
from controllers.download_controller import baixar_arquivo_controller

download_bp = Blueprint('download', __name__)

@download_bp.route('/<nome_arquivo>', methods=['GET'])
def download(nome_arquivo):
    return baixar_arquivo_controller(nome_arquivo)
