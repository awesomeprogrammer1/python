from collections import Counter

"""
Write a function search_substr(subst, st) that takes 2 strings 
and determines if the substring subst is in the string st.
If the substring is found, the phrase "There is a contact!" 
is returned, otherwise "Missed!".
A match must be found regardless of the case of both strings.

"""


# def search_substr(subst: str, st: str) -> str:
#     if subst.lower() in st.lower():
#         return "There is a contact!"
#     else:
#         return "Missed!"


# Тесты
# print(search_substr("Кол", "коЛокОл"))
# print(search_substr("Колобок", "колобоК"))
# print(search_substr("Кол", "Плов"))

"""
It is required to determine the indices of the first and last occurrence of a letter in a string.
To do this, you need to write the first_last(letter, st) function, which includes 2 parameters: letter is the search character, st is the target string.
If there is no letter in the string, you need to return a tuple (None, None), if it is, then the tuple will consist of the first and last index of this character.


"""
# хоккей


# def first_last(letter: str, st: str) -> tuple:
#     if letter in st:
#         return (st.index(letter), st.rindex(letter))
#     else:
#         return (None, None)


# print(first_last('a', 'abba'))
# print(first_last('a', 'abbaaaab'))
# print(first_last('a', 'a'))
# print(first_last('a', 'spring'))


"""
Based on the provided passage of text, determine the 3 most common characters in it.
Spaces should be ignored (not taken into account when counting).
To display the results of calculations, you need to write the top3(st) function.
Present the result of the function as a string: "symbol - number of times, symbol - number of times ...".

"""


def top3(st: str) -> str:
    symbol_count: dict = {}
    for symbol in st:
        if symbol != " ":
            symbol_count[symbol] = len()
    print(symbol_count)
    return "e"


print(top3("asdajeefrse"))
