def replace(s: str, old_char: str, new_char: str) -> str:

    for x in s:
        if x == old_char:
            x = new_char

    return s

def function_in(s: str, char: str) -> bool:
    

str_var = "Hello, World"
print(str_var)

str_var = replace(str_var, "H", "J")
print(str_var)

