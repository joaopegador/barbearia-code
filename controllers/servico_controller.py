from models.servico_model import listar_servicos

def listar_servicos_controller():
    servicos = listar_servicos()

    if not servicos:
        return {"mensagem": "Nenhum serviço encontrado."}, 200

    lista_servicos = [
        {"id": servico["id"], "nome": servico["nome"]}
        for servico in servicos
    ]

    return {"servicos": lista_servicos}, 200
