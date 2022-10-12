hey = ["hi", "andrew"]


def join_func(list1: list, seperator: str):
    remove_brackets = str(list1)[1:-1]
    seperator_input = remove_brackets.replace(",", seperator)
    print(seperator_input)


join_func(hey, "...")
