def replace(s: str, old_char: str, new_char: str) -> str:
    new_s = ""
    for element in s:
        if element in old_char:
            if new_s in new_char:
                if element in old_char:
                    new_s += element
                    # for element in new_s
                else:
                    pass
            else:
                if new_s == new_char:
                    new_s += new_char
                else:
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
    print(replace("Hello", "ll", "mm"))
