def replace(s: str, old_char: str, new_char: str) -> str:
    new_s = ""
    for element in s:
        if element == old_char:
            new_s += new_char
        else:
            if element in old_char:
                new_s += new_char
            else:
                new_s += element
    return new_s


def function_in(s: str, char: str) -> bool:
    for element in s:
        if element == char:
            return True
    return False


if __name__ == "__main__":
    print(replace("Hello", "He", "Y"))
