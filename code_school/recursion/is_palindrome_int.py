def is_palindrome_int(num) -> bool:
    str_num = str(num)
    if str_num[0] != str_num[len(str_num)-1]:
        return False
    elif int(str_num) < 10:
        return True
    elif int(str_num) < 100:
        return str_num[0] == str_num[len(str_num)-1]
    elif str_num[0] == str_num[len(str_num)-1]:
        return is_palindrome_int(str_num[1:len(str_num)-1])


print(is_palindrome_int(101))

