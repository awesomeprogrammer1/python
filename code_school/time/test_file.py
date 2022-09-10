from datetime import datetime

date_string = "21 June, 2018"

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_string =", date_object)
