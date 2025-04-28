import sqlite3
from config import BANCO_DE_DADOS

def obter_conexao():
    conn = sqlite3.connect(BANCO_DE_DADOS)
    conn.row_factory = sqlite3.Row
    return conn

def salvar_upload(filename, user_id, upload_date):
    conn = obter_conexao()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO uploads (filename, user_id, upload_date)
            VALUES (?, ?, ?)
        """, (filename, user_id, upload_date))
        conn.commit()
        return True
    except Exception as e:
        print(f"Erro ao salvar upload: {e}")
        return False
    finally:
        conn.close()
