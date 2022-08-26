import telebot

config = {
    "name": "FluffyAndy_Bot",
    "token": "5637600030:AAEcH6SkSx9KqVq1f_kYNT_WkKIlB37Oux4",
}

bot = telebot.TeleBot(config["token"])

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, "Hello, User.")


bot.polling(non_stop=True, interval=0)
