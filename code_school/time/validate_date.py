import datetime


def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    print(date_text)

if __name__ == "__main__":
    date_var = input("Input a date in the yyyy-mm-dd format: ")
    validate(date_var)
