def replace(s: str, old_char: str, new_char: str) -> str:
    for element in s:
        if old_char in s:
            if len(old_char) > 2:
                s_split = s.split(old_char)
                for i in range(len(s_split)):
                    if s_split[i] == "":
                        s_split.insert(i, new_char)
                        s_join = "".join(s_split)
                        return s_join
            else:
                if element in old_char:
                    s_split2 = s.split(old_char)
                    for i in range(len(s_split2)):
                        if s_split2[i] == "":
                            s_split2.insert(i, new_char)
                            s_join2 = "".join(s_split2)
                            return s_join2
                    else:
                        s_split2.insert(i, new_char)
                        s_join2 = "".join(s_split2)
                        return s_join2
        else:
            return s


def replace2(s: str, old_str: str, new_str: str) -> str:
    list_var = s.split(old_str)
    return new_str.join(list_var)


print(replace("Hello", "He", "Yo"))
print(replace2("Hello", "He", "Yo"))
