import os
import logging
from flask import request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_jwt_extended import get_jwt_identity, jwt_required

LOG_FILE = "uploads.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

PASTA_UPLOAD = 'uploads'

if not os.path.exists(PASTA_UPLOAD):
    os.makedirs(PASTA_UPLOAD)

class UploadController:

    @staticmethod
    @jwt_required()
    def upload_file():
        user_id = get_jwt_identity()

        if 'file' not in request.files:
            return jsonify({"erro": "Nenhum arquivo enviado"}), 400

        arquivo = request.files['file']

        if arquivo.filename == '':
            return jsonify({"erro": "Nome do arquivo vazio"}), 400

        nome_arquivo = secure_filename(arquivo.filename)
        nome_final = f"user{user_id}_{nome_arquivo}"
        caminho = os.path.join(PASTA_UPLOAD, nome_final)
        arquivo.save(caminho)

        logging.info(f"Upload OK: {nome_final} | Usuário: {user_id} | IP: {request.remote_addr}")

        return jsonify({"mensagem": "Arquivo enviado com sucesso!", "arquivo": nome_final}), 200

    @staticmethod
    @jwt_required()
    def listar_arquivos():
        user_id = get_jwt_identity()
        arquivos_usuario = [
            f for f in os.listdir(PASTA_UPLOAD)
            if f.startswith(f"user{user_id}_")
        ]
        return jsonify({"arquivos": arquivos_usuario}), 200

    @staticmethod
    @jwt_required()
    def deletar_arquivo(nome_arquivo):
        user_id = get_jwt_identity()
        nome_seguro = secure_filename(nome_arquivo)
        nome_completo = f"user{user_id}_{nome_seguro}"
        caminho = os.path.join(PASTA_UPLOAD, nome_completo)

        if os.path.exists(caminho):
            os.remove(caminho)
            logging.info(f"Arquivo deletado: {nome_completo} | Usuário: {user_id}")
            return jsonify({"mensagem": "Arquivo deletado com sucesso"}), 200
        else:
            return jsonify({"erro": "Arquivo não encontrado"}), 404
