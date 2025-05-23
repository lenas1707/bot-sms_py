import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configurações do Twilio
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
SEU_NUMERO = os.getenv('SEU_NUMERO')

# Verifica se as credenciais foram carregadas
if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, SEU_NUMERO]):
    print("ERRO: Credenciais do Twilio não encontradas!")
    print("Por favor, verifique se o arquivo .env existe e contém todas as credenciais necessárias:")
    print("TWILIO_ACCOUNT_SID=seu_account_sid")
    print("TWILIO_AUTH_TOKEN=seu_auth_token")
    print("TWILIO_PHONE_NUMBER=seu_numero_twilio")
    print("SEU_NUMERO=seu_numero_celular")
    exit(1)

# Configurações dos lembretes
LEMBRETES = [
    {
        "horario": "09:30",
        "mensagem": "Lembrete 1"
    },

    {
        "horario": "13:30",
        "mensagem": "Lembrete 2"
    }
]