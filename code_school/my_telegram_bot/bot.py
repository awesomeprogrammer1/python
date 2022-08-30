import telebot
from datetime import date
import time

config = {
    "name": "FluffyAndy_Bot",
    "token": "5637600030:AAEcH6SkSx9KqVq1f_kYNT_WkKIlB37Oux4",
}

bot = telebot.TeleBot(config["token"])
today = date.today()
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    user_message = message.text
    message_var = user_message.lower()
    if message_var == "hello":
        bot.send_message(message.chat.id, "Hello, User.")
    if message_var == "date":
        bot.send_message(message.chat.id, today)
    if message_var == "time":
        bot.send_message(message.chat.id, current_time)
    if message_var == "how are you":
        bot.send_message(message.chat.id, "I am very good, thank you.")


bot.polling(non_stop=True, interval=0)
