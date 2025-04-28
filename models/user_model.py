import sqlite3 
from config import BANCO_DE_DADOS

def obter_conexao():
    conn = sqlite3.connect(BANCO_DE_DADOS)
    conn.row_factory = sqlite3.Row
    return conn

class UsuarioModelo:
    @staticmethod
    def criar_usuario(username, password, email):
        conn = obter_conexao()
        try:
            conn.execute('INSERT INTO users (username, password, email) VALUES (?, ?, ?)', (username, password, email))
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()
            
    @staticmethod
    def buscar_por_username(username):
        conn = obter_conexao()
        try:
            usuario = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
            return usuario
        finally:
            conn.close()

    @staticmethod
    def buscar_por_email(email):
        conn = obter_conexao()
        try:
            usuario = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
            return usuario
        finally:
            conn.close()
