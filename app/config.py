# config.py

# Configurações gerais
APP_NAME = "MeuApp"
VERSION = "1.0.0"
DEBUG = True

# Configurações de banco de dados
DATABASE = {
    'host': 'localhost',
    'port': 5432,
    'user': 'usuario',
    'password': 'senha',
    'database': 'meu_banco_de_dados'
}

# Configurações de API
API_KEY = 'minha-chave-de-api'
API_URL = 'https://api.exemplo.com/'

# Configurações de email
EMAIL_CONFIG = {
    'smtp_server': 'smtp.exemplo.com',
    'smtp_port': 587,
    'email': 'meuemail@exemplo.com',
    'password': 'minhasenha'
}

# Configurações de logging
LOGGING_LEVEL = 'DEBUG'
LOG_FILE = 'app.log'