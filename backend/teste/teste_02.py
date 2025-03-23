import telebot

BOT_TOKEN = "7294948712:AAEj57qIFRaXmS8ZB__0nq6SETufOIb6hzQ"
CHAT_ID = "5588207726"

def enviar_mensagem(mensagem):
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(CHAT_ID, mensagem)

enviar_mensagem("Teste de mensagem direta do bot Telegram!")
