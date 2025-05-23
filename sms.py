from twilio.rest import Client
from datetime import datetime
import time
import schedule
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_PHONE_NUMBER,
    SEU_NUMERO,
    LEMBRETES
)

def enviar_sms(mensagem):
    """Envia um SMS usando o Twilio."""
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        msg = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            to=SEU_NUMERO, # API versão gratuita só suporta numeros de contas cadastradas no Twilio
            body=mensagem
        )
        print(f"SMS enviado com sucesso: {mensagem}")
        return True
    except Exception as e:
        print(f"Erro ao enviar SMS: {str(e)}")
        return False

def agendar_lembretes():
    """Agenda os lembretes de acordo com os horários configurados."""
    for lembrete in LEMBRETES:
        schedule.every().day.at(lembrete["horario"]).do(
            enviar_sms, mensagem=lembrete["mensagem"]
        )
        print(f"Lembrete agendado para {lembrete['horario']}")

def main():
    print("Iniciando sistema de lembretes de medicamentos...")
    print("Pressione Ctrl+C para encerrar o programa")
    

    agendar_lembretes()
    

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()