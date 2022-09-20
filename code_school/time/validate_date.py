import datetime


def is_valid_date(date_text: str, date_format_type: str) -> bool:
    try:
        datetime.datetime.strptime(date_text, date_format_type)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    date_type_var = input("Input the date format you are using. \nExample: %Y-%m-%d. Format can't be empty. ")
    date_var = input("Input a date in your format to check if it is valid: ")
    print(is_valid_date(date_var, date_type_var))