# models/agendamento_model.py

import sqlite3
from config import BANCO_DE_DADOS

def obter_conexao():
    conn = sqlite3.connect(BANCO_DE_DADOS)
    conn.row_factory = sqlite3.Row
    return conn

def criar_agendamento(usuario_id, barbeiro_id, servico_id, data, hora):
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO agendamentos (usuario_id, barbeiro_id, servico_id, data, hora)
            VALUES (?, ?, ?, ?, ?)
        """, (usuario_id, barbeiro_id, servico_id, data, hora))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao criar agendamento: {e}")
        return False
    finally:
        conn.close()

def listar_agendamentos_por_usuario(usuario_id):
    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT a.id, a.data, a.hora, a.status, b.nome AS barbeiro, s.nome AS servico
            FROM agendamentos a
            JOIN barbeiros b ON a.barbeiro_id = b.id
            JOIN servicos s ON a.servico_id = s.id
            WHERE a.usuario_id = ?
        """, (usuario_id,))
        agendamentos = cursor.fetchall()
        return agendamentos
    except Exception as e:
        print(f"Erro ao listar agendamentos: {e}")
        return []
    finally:
        conn.close()

