from models.agendamento_model import criar_agendamento, listar_agendamentos_por_usuario

def criar_agendamento_controller(usuario_id, servico_id, data, hora):
    sucesso = criar_agendamento(usuario_id, servico_id, data, hora)

    if sucesso:
        return {"mensagem": "Agendamento criado com sucesso."}, 201
    else:
        return {"erro": "Erro ao criar agendamento."}, 500

def listar_agendamentos_usuario_controller(usuario_id):
    agendamentos = listar_agendamentos_por_usuario(usuario_id)

    if not agendamentos:
        return {"mensagem": "Nenhum agendamento encontrado."}, 200

    agendamento_lista = []
    for agendamento in agendamentos:
        agendamento_lista.append({
            "id": agendamento["id"],
            "data": agendamento["data"],
            "hora": agendamento["hora"],
            "status": agendamento["status"],
            "servico": agendamento["servico"]
        })

    return {"agendamentos": agendamento_lista}, 200
