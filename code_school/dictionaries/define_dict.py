dict_var = {}


value_of_a = 8

# if "a" in dict_var.keys():
#     dict_var["a"] = value_of_a
# else:
#     value_of_a = 0

# print(value_of_a)

# if "a" in dict_var.keys():
#     dict_var["a"] = value_of_a+1
# else:
#     value_of_a = 1


print(value_of_a)

def top3(st: str) -> str:
    symbol_count: dict = {}
    value_of_symbol = 0
    for symbol in st:
        if symbol in symbol_count.keys():
            value_of_symbol += 1
        if symbol != " ":
            symbol_count[symbol] = value_of_symbol
    print(symbol_count)
    return "e"

print(top3("col caun lreo"))

            
                