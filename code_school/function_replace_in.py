def replace(s: str, old_char: str, new_char: str) -> str:

    for x in s:
        if x == old_char:
            x = new_char

    return s


def function_in(s: str, char: str) -> bool:
    for x in s:
        if x == char:
            return True
    return False


if __name__ == "__main__":
    print(function_in("hedgie", "d"))
