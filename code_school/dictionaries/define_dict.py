dict_var = {}


value_of_a = 8

# if "a" in dict_var.keys():
#     dict_var["a"] = value_of_a
# else:
#     value_of_a = 0

# print(value_of_a)

if "a" in dict_var.keys():
    dict_var["a"] = value_of_a+1
else:
    value_of_a = 1


print(value_of_a)

def top3(st: str) -> str:
    symbol_count: dict = {}
    for symbol in st:
        if symbol != " ":
            symbol_count[symbol] = 0
            if symbol in symbol_count:
                symbol_count[symbol] = +1
    print(symbol_count)
    return "e"

print(top3("coolcaunlreo"))

            
                