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
    print(replace("Hello", "He", "Yo"))
    print(replace("Hello", "ll", "mm"))
