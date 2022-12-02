import telebot
from datetime import date, datetime
import time
import os.path
import json
from pathlib import Path

path1 = os.path.join("code_school", "bot_task_output.txt")

config = {
    "name": "FluffyAndy_Bot",
    "token": "5637600030:AAEcH6SkSx9KqVq1f_kYNT_WkKIlB37Oux4",
}

bot = telebot.TeleBot(config["token"])
today = date.today()
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
path = Path("code_school\\my_telegram_bot")
user_db = path / "login_info.json"


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.lower() == "start":
        bot.send_message(
            message.chat.id,
            "Register or Authenticate yourself with 'register' and/or 'authenticate' to use commands",
        )
    elif message.text.lower() == "register":
        user_password = bot.send_message(message.chat.id, "Enter a password")
        bot.register_next_step_handler(user_password, registration)
    elif message.text.lower() == "authenticate":
        authenticate_user = bot.send_message(message.chat.id, "Enter your password")
        bot.register_next_step_handler(authenticate_user, authentication)
        if authentication(message.chat.id) == False:
            bot.send_message(
                message.chat.id,
                "Authentication failed, please enter 'start' to restart the process",
            )
        else:
            if message.text.lower() == "hello":
                bot.send_message(message.chat.id, "Hello, User.")
            elif message.text.lower() == "date":
                bot.send_message(message.chat.id, today)
            elif message.text.lower() == "time":
                bot.send_message(message.chat.id, t)
            elif message.text.lower() == "how are you":
                bot.send_message(message.chat.id, "I am very good, thank you.")
            elif message.text.lower() == "calculator":
                action = bot.send_message(
                    message.chat.id, "Enter operation"
                )  # 2+ 2 -> 4
                bot.register_next_step_handler(action, calculator)
            elif message.text.lower() == "length":
                action2 = bot.send_message(
                    message.chat.id, "Enter any amount of characters"
                )
                bot.register_next_step_handler(action2, length)
            elif message.text.lower() == "count":
                action3 = bot.send_message(message.chat.id, "Enter a sentence ")
                bot.register_next_step_handler(action3, count_words)
            elif message.text.lower() == "textinfo":
                action4 = bot.send_message(message.chat.id, "Enter a piece of text")
                bot.register_next_step_handler(action4, text_info)
            else:
                bot.send_message(
                    message.chat.id,
                    "Hello! I am a bot that can help you. Avalible commands include hello, date, time, how are you, textinfo, calculator, and length",
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


def text_info(message):
    file1 = open(path1, "w")
    vowels = ["a", "e", "i", "o", "u"]
    consonants = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    counter_v = 0
    counter_c = 0
    digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = [",", ".", "/", "!", "?"]
    symbol_counter = 0
    number_counter = 0
    length_message = len(message.text.split())
    for char in message.text:
        if char in vowels:
            counter_v += 1
        if char in digits:
            number_counter += 1
        if char in symbols:
            symbol_counter += 1
        if char in consonants:
            counter_c += 1
    file1.write(
        f"Amount of characters: {len(message.text)}. Number of Vowels: {counter_v}. Number of Consonants: {counter_c}. Number of digits: {number_counter}. Number of symbols: {symbol_counter}. Number of words: {length_message}"
    )
    bot.send_message(message.chat.id, "Information sent to destination file")
    file1.close()


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
        list_of_words.append(f"{word} - {words2.count(word)}")
    bot.send_message(message.chat.id, ", ".join(list_of_words))


def registration(message):
    get_info = open(user_db, "r")
    get_user_info = json.load(get_info)
    get_info.close()
    get_user_info[message.chat.id] = message.text
    write_info = open(user_db, "w")
    json.dump(get_user_info, write_info)
    write_info.close()
    bot.send_message(message.chat.id, "Registration Complete")


def authentication(message):
    get_info = open(user_db, "r")
    get_user_info = json.load(get_info)
    get_info.close()
    return message.text in get_user_info[message.chat.id]


bot.polling(non_stop=True, interval=0)


# text {word:count(word)}
# my name is my Andrew {"my": 2, "name": 1, ....}
