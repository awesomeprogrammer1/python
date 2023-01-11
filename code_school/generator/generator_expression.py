# list_var = list()
# for i in range(101):
#     list_var.append(i)
# print(list_var)

# list_var = [i for i in range(101)]
# print(list_var)

# list_var = [i for i in range(101) if i % 2 == 0]
# print(list_var)

list_of_strings = [
    "Список - изменяемый тип данных",
    "Строка - неизменяемый тип данных",
    "Строковый метод работает быстрее, чем срез",
    "Для обхода последовательности используйте совместный цикл",
]
list_of_str_elements = [element for element in list_of_strings if element[0] == "С"]
print(list_of_str_elements)
