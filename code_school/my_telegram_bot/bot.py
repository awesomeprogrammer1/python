import telebot
from datetime import date, datetime
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

    if message.text.lower() == "hello":
        bot.send_message(message.chat.id, "Hello, User.")
    elif message.text == "date":
        bot.send_message(message.chat.id, today)
    elif message.text.lower() == "time":
        bot.send_message(message.chat.id, t)
    elif message.text.lower() == "how are you":
        bot.send_message(message.chat.id, "I am very good, thank you.")
    elif message.text.lower() == "calculator":
        action = bot.send_message(message.chat.id, "Enter operation")  # 2+ 2 -> 4
        bot.register_next_step_handler(action, calculator)
    elif message.text.lower() == "length":
        action2 = bot.send_message(message.chat.id, "Enter any amount of characters")
        bot.register_next_step_handler(action2, length)
    if message.text.lower() == "count":
        action3 = bot.send_message(message.chat.id, "Enter a sentence ")
        bot.register_next_step_handler(action3, count_words)
    else:
        bot.send_message(
            message.chat.id,
            "Hello! I am a bot that can help you. Avalible commands include hello, date, time, how are you, calculator, and length",
        )


def calculator(message):
    symbols = ["+", "-", "*", "/"]
    for s in symbols:
        if s in message.text:
            numbers = message.text.split(s)  # ['2', '2']
            if s == "+":
                add = int(numbers[0]) + int(numbers[1])
                bot.send_message(message.chat.id, add)
            if s == "-":
                subtract = int(numbers[0]) - int(numbers[1])
                bot.send_message(message.chat.id, subtract)
            if s == "*":
                multiply = int(numbers[0]) * int(numbers[1])
                bot.send_message(message.chat.id, multiply)
            if s == "/":
                try:
                    divide = int(numbers[0]) / int(numbers[1])
                    bot.send_message(message.chat.id, divide)
                except ZeroDivisionError:
                    bot.send_message(message.chat.id, "Cannot divide by Zero")


def length(message):
    bot.send_message(message.chat.id, len(message.text))


def count_words(message):
    # 1st approach 
    # dict_of_words = {}
    # words = message.text.split()
    # for word in words:
    #     list_of_words[word] = words.count(word)
    # for element in list_of_words:
    #     bot.send_message(message.chat.id, f'{element}- {list_of_words.get(element)}')
    # 2nd approach
    list_of_words = []
    words2 = message.text.split()
    for word in words2:
        list_of_words.append(f'{word} - {words2.count(word)}')
    bot.send_message(message.chat.id, ", ".join(list_of_words))

bot.polling(non_stop=True, interval=0)

# text {word:count(word)}
# my name is my Andrew {"my": 2, "name": 1, ....}
