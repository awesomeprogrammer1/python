def replace(s: str, old_char: str, new_char: str) -> str:
    new_s = ""
    for element in s:
        if element in old_char:
            if new_s in new_char:
                if element in old_char:
                    if new_s == new_char:
                        new_s += element
                else:
                    pass
            else:
                if new_s == new_char:
                    new_s += new_char
                else:
                    new_s += new_char
        else:
            new_s += element
    newest_s = new_s.replace(old_char, new_char)
    return newest_s

# def replace2(s: str, find: str, replace: str) -> str:
#     result = ""
#     for i in range(len(s)):
#         found_match = False
#         if s[i] == find[i] and i + len(find) < len(s):
#             for j in range(len(find)):
#                 if s[i+j] != find[j]:
#                     break
#             else:
#                 found_match = True
#     split_list = s.split(find)
#     return replace.join(split_list)


def function_in_papa(s: str, find: str) -> bool:
    for i in range(len(s)):
        if s[i] == find[0] and i + len(find) <= len(s):
            for j in range(1, len(find)):
                if s[i + j] != find[j]:
                    break
            else:
                return True
    return False


if __name__ == "__main__":
    print(function_in_papa("Andrew", "An"))
