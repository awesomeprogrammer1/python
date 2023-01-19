# list_var = list()
# for i in range(101):
#     list_var.append(i)
# print(list_var)

# list_var = [i for i in range(101)]
# print(list_var)

# list_var = [i for i in range(101) if i % 2 == 0]
# print(list_var)

# list_of_strings = [
#     "Список - изменяемый тип данных",
#     "Строка - неизменяемый тип данных",
#     "Строковый метод работает быстрее, чем срез",
#     "Для обхода последовательности используйте совместный цикл",
# ]
# list_of_str_elements = [element for element in list_of_strings if "тип данных" in element]
# print(list_of_str_elements)

# key = number, value = number*2
# dict_var = {number: number * 2 for number in range(1, 101)}
# print(dict_var)


# list_of_strings = [
#     "Список - изменяемый тип данных",
#     "Строка - неизменяемый тип данных",
#     "Строковый метод работает быстрее, чем срез",
#     "Для обхода последовательности используйте совместный цикл",
# ]
# dict_var = {element: len(element) for element in list_of_strings}
# print(dict_var)


# papa {"p":2,"a":2}
word = input("Enter a word: ")
word_dict = {character: word.count(character) for character in word}
print(word_dict)


# andrew is good boy 
# {'andrew': {'a':1,'n':1...} , 'is': {'i':1,'s':1},...}

words = input("Enter a sentence: ").split()
word_dict = { : {}}

