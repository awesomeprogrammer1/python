dict_var = {}


# value_of_a = 8

# if "a" in dict_var.keys():
#     dict_var["a"] = value_of_a
# else:
#     value_of_a = 0

# print(value_of_a)

# if "a" in dict_var.keys():
#     dict_var["a"] = value_of_a+1
# else:
#     value_of_a = 1


# print(value_of_a)

"""
Based on the provided passage of text, determine the 3 most common characters in it.
Spaces should be ignored (not taken into account when counting).
To display the results of calculations, you need to write the top3(st) function.
Present the result of the function as a string: "symbol - number of times, symbol - number of times ...".

"""


def top3(st: str) -> str:
    symbol_count: dict = {}
    for symbol in st:
        if symbol == " ":
            continue
        if symbol not in symbol_count:
            symbol_count[symbol] = 1
        else:
            symbol_count[symbol] += 1
    ordered_symbols = sorted(symbol_count.items(), key=lambda x:x[1], reverse=True)
    top3_symbols = ordered_symbols[:3]
    return f"Symbol: {top3_symbols[0][0]} | Number of occurences: {top3_symbols[0][1]}. Symbol: {top3_symbols[1][0]} | Number of occurences: {top3_symbols[1][1]}. Symbol: {top3_symbols[2][0]} | Number of occurences: {top3_symbols[2][1]}"
    

print(top3("col caun lreo"))


            
                