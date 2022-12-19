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
SECONDS_IN_24_HOURS = 86400
print(t)

# def is_authenticated():
#     def inner_is_authenticated():
#         return False
#     return inner_is_authenticated()


user_db_handle = open(user_db, "r")
user_db_dict = json.load(user_db_handle)
user_db_handle.close()



@bot.message_handler(content_types=["text"])
# @is_authenticated()
def handle_text(message):
    if is_authenticated(message.chat.id) is True:
        if message.text.lower() == "help":
            bot.send_message(message.chat.id, "Avalible commands: \n 'hello' \n 'date' \n 'time' \n 'how are you' \n 'calculator' \n 'length' \n 'count' \n 'textinfo'")
        elif message.text.lower() == "hello":
            bot.send_message(message.chat.id, "Hello, User.")
        elif message.text.lower() == "date":
            bot.send_message(message.chat.id, today)
        elif message.text.lower() == "time":
            bot.send_message(message.chat.id, current_time)
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
            bot.send_message(message.chat.id, "Error: Your command was not recognized: type 'help' for a list of commands ")
    else:
        if str(message.chat.id) not in user_db_dict:
            bot.send_message(message.chat.id, "Please register by typing 'register'",)
            if message.text.lower() == "register":
                user_password = bot.send_message(message.chat.id, "Enter a password")
                bot.register_next_step_handler(user_password, registration)
        else:
            bot.send_message(message.chat.id, "Please Authenticate by typing 'authenticate'",)
            if message.text.lower() == "authenticate":
                authenticate_user = bot.send_message(message.chat.id, "Enter your password")
                bot.register_next_step_handler(authenticate_user, user_authenticated)


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
    user_db_handle = open(user_db, "r")
    user_db_dict = json.load(user_db_handle)
    user_db_handle.close()
    user_db_dict[str(message.chat.id)] = {"password": message.text}
    write_info = open(user_db, "w")
    json.dump(user_db_dict, write_info)
    write_info.close()
    bot.send_message(message.chat.id, "Registration Complete")


'''
def is_authenticated(message):
    get_info = open(user_db, "r")
    get_user_info = json.load(get_info)
    get_info.close()
    return message.text in get_user_info[message.chat.id]
'''


'''
This function authenticates the user
'''


def user_authenticated(message):
    user_db_handle = open(user_db, "r")
    user_db_dict = json.load(user_db_handle)
    user_db_handle.close()
    if message.text == user_db_dict.get(str(message.chat.id)).get("password"):
        bot.send_message(message.chat.id, "Successfully Authenticated. Type 'help' for a full list of commands when authenticated")
        update_authentication_timestamp(message.chat.id, time.time())
    else:
        bot.send_message(message.chat.id, "Password Incorrect")


def update_authentication_timestamp(user_id, timestamp):
    user_db_handle = open(user_db, "r")
    user_db_dict = json.load(user_db_handle)
    user_db_handle.close()
    user_db_dict[str(user_id)]["time"] = int(timestamp)
    print(user_db_dict)
    user_db_handle = open(user_db, "w")
    json.dump(user_db_dict, user_db_handle)
    user_db_handle.close()


'''
def is_authenticated(authentication_timestamp):
    def inner_is_authenticated():
        if int(time.time()) - int(authentication_timestamp) < 86400:
            return True
        else:
            return False
    return inner_is_authenticated()
'''


def is_authenticated(user_id):
    user_db_handle = open(user_db, "r")
    user_db_dict = json.load(user_db_handle)
    user_db_handle.close()
    if str(user_id) not in user_db_dict:
        return False
    if "time" not in user_db_dict[str(user_id)]:
        return False
    authentication_timestamp = user_db_dict[str(user_id)]["time"]
    if int(time.time()) - authentication_timestamp < 86400:
        return True
    else:
        return False


bot.polling(non_stop=True, interval=0)


# text {word:count(word)}
# my name is my Andrew {"my": 2, "name": 1, ....}
