# models/servico_model.py

import sqlite3
from config import BANCO_DE_DADOS

def obter_conexao():
    conn = sqlite3.connect(BANCO_DE_DADOS)
    conn.row_factory = sqlite3.Row
    return conn

def listar_servicos():
    conn = obter_conexao()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id, nome FROM servicos
        """)
        servicos = cursor.fetchall()
        return servicos
    except Exception as e:
        print(f"Erro ao listar serviços: {e}")
        return []
    finally:
        conn.close()

