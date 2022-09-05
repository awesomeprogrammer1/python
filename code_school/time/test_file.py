from datetime import datetime
import calendar

try:
    verify_date = input("Enter a date with the yyyy-mm-dd format ")
except ValueError:
    print("Error, invalid date")
verify_date_parts = verify_date.split("-")
if int(verify_date_parts[1]) > 12 or int(verify_date_parts[2]) > 31:
    print("Error, invalid date")
else:
    if (
        calendar.isleap == True
        and int(verify_date_parts[1]) == 2
        and int(verify_date_parts[2]) >= 29
    ):
        print(verify_date)
    else:
        print("Error, Invalid Date")
