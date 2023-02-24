def is_palindrome(st: str) -> bool:
    return st == __reverse_str(st)
    

def __reverse_str(st: str) -> str:
    reversed_st = []
    for i in range(len(st)-1, -1, -1):
        reversed_st.append(st[i])
    return "".join(reversed_st)



