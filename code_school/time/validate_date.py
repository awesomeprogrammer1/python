import datetime


def is_valid_date(date_text: str) -> bool:
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    date_var = input("Input a date in the yyyy-mm-dd format: ")
    is_valid_date(date_var)
