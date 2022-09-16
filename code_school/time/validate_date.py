import datetime


def is_valid_date(date_text: str, date_format_type: str) -> bool:
    if date_format_type.lower() == "international":
        try:
            datetime.datetime.strptime(date_text, "%Y-%m-%d")
            return True
        except ValueError:
            return False
    if date_format_type.lower() == "american":
        try:
            datetime.datetime.strptime(date_text, "%m/%d/%Y")
            return True
        except ValueError:
            return False
    if date_format_type.lower() == "european":
        try:
            datetime.datetime.strptime(date_text, "%d/%m/%Y")
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    date_type_var = input("Input the date format you would like: ")
    date_var = input("Input a date in your format to check if it is valid: ")
    print(is_valid_date(date_var, date_type_var))
