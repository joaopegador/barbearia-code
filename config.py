import os

# Configurações do Banco de Dados
BANCO_DE_DADOS = 'banco.db'

# Configurações de E-mail
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USERNAME = 'joaopedrob681@gmail.com'
MAIL_PASSWORD = 'jyer epvq jltm ooju'  # Use variáveis de ambiente para credenciais sensíveis
MAIL_USE_TLS = True
MAIL_USE_SSL = False

# Configurações de JWT
SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave-secreta-123'
JWT_SECRET_KEY = SECRET_KEY  # Flask-JWT-Extended usa isso

# Configuração de upload
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Usando o diretório atual + 'uploads'

# Criar a pasta de uploads caso ela não exista
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
