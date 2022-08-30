import telebot
from datetime import date
import time

config = {
    "name": "FluffyAndy_Bot",
    "token": "5637600030:AAEcH6SkSx9KqVq1f_kYNT_WkKIlB37Oux4",
}

bot = telebot.TeleBot(config["token"])


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hello" or "hello":
        bot.send_message(message.chat.id, "Hello, User.")
    if message.text == "Date" or "date":
        today = date.today()
        bot.send_message(message.chat.id, today)
    if message.text == "Time" or "time":
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        bot.send_message(message.chat.id, current_time)
    if message.text == "How are you" or "how are you":
        bot.send_message(message.chat.id, "I am very good, thank you.")


bot.polling(non_stop=True, interval=0)
