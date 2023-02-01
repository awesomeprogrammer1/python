order_str = [
    "Список - изменяемый тип данных",
    "Строка - неизменяемый тип данных",
    "Строковый метод работает быстрее, чем срез",
    "Для обхода последовательности используйте совместный цикл"]

more_than_4_order_str = [element for element in order_str if len(element.replace("-", "").split()) > 4]
print(more_than_4_order_str)