import os
from flask import send_from_directory
from config import UPLOAD_FOLDER  # Agora pega do config!

def baixar_arquivo_controller(nome_arquivo):
    caminho_arquivo = os.path.join(UPLOAD_FOLDER, nome_arquivo)

    if not os.path.exists(caminho_arquivo):
        return {"erro": "Arquivo não encontrado."}, 404

    return send_from_directory(UPLOAD_FOLDER, nome_arquivo, as_attachment=True)
def salvar_arquivo(arquivo):
    caminho_arquivo = os.path.join(UPLOAD_FOLDER, arquivo.filename)
    arquivo.save(caminho_arquivo)
    return caminho_arquivo
