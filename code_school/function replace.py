def replace(s: str, old_char: str, new_char: str) -> str:

    for x in s:
        if x == old_char:
            x = new_char
            s.replace(old_char, x)
    return s


print(replace("Hello World", "H", "J"))
