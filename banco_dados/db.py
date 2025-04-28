import sqlite3
import logging
from config import BANCO_DE_DADOS

def obter_conexao():
    conn = sqlite3.connect(BANCO_DE_DADOS)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    conn = obter_conexao()
    cursor = conn.cursor()

    # Tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)

    # Tabela de uploads
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS uploads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            upload_date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    # Tabela de downloads
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS downloads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT NOT NULL,
            user_id INTEGER,
            ip TEXT,
            download_date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)

    # Tabela de serviços
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS servicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """)

    # Tabela de agendamentos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            servico_id INTEGER NOT NULL,
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            status TEXT DEFAULT 'pendente',
            FOREIGN KEY (usuario_id) REFERENCES users(id),
            FOREIGN KEY (servico_id) REFERENCES servicos(id)
        )
    """)

    # Tabela de endereços
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enderecos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            rua TEXT NOT NULL,
            numero TEXT NOT NULL,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            cep TEXT NOT NULL,
            FOREIGN KEY(usuario_id) REFERENCES users(id)
        )
    """)

    # Seed de serviços
    cursor.execute('SELECT COUNT(*) FROM servicos')
    servicos_existem = cursor.fetchone()[0]

    if servicos_existem == 0:
        cursor.executemany("""
            INSERT INTO servicos (nome) VALUES (?)
        """, [
            ('Corte Masculino',),
            ('Barba',),
            ('Corte + Barba',),
            ('Sobrancelha',),
        ])
        logging.info("[✓] Serviços iniciais inseridos.")

    conn.commit()
    conn.close()
    logging.info("[✓] Tabelas criadas/atualizadas com sucesso.")

if __name__ == "__main__":
    criar_tabelas()
