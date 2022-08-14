from operator import index


def replace(s: str, old_char: str, new_char: str) -> str:
    new_s = ""
    for x in s:
        if x == old_char:
            x = new_char
            new_s += x
        else:
            new_s += x
    return new_s


def function_in(s: str, char: str) -> bool:
    for x in s:
        if x == char:
            return True
    return False


if __name__ == "__main__":
    print(replace("Hello", "H", "Y"))
