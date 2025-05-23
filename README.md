# Sistema de Envio de SMS

Este é um sistema Python para envio de mensagens SMS utilizando a API Twilio. Criado para auxiliar minha mãe a lembrar de tomar os remédios após uma cirurgia

## Requisitos

- Python 3.x
- Conta Twilio (com credenciais de API)
- Dependências listadas em `requirements.txt`

## Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure suas credenciais:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione suas credenciais Twilio:
   ```
   TWILIO_ACCOUNT_SID=seu_account_sid
   TWILIO_AUTH_TOKEN=seu_auth_token
   TWILIO_PHONE_NUMBER=seu_numero_twilio
   ```

## Uso

Execute o script principal:
```bash
python sms.py
```

## Estrutura do Projeto

- `sms.py`: Script principal para envio de mensagens
- `config.py`: Configurações e funções auxiliares, onde estão os lembretes
- `requirements.txt`: Lista de dependências do projeto

## Dependências

- twilio==8.10.0
- schedule==1.2.0
- python-dotenv==1.0.0
