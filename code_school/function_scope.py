# a = 5
# def test():
#     return a + 3


# sun(time), time: "06:00", "11:30",
# return an angle-str  ,
# "06:00"-0, "12:00"- 90, "18:00"-180,


dict = {}
list = []


def sun2(hours: int, minutes: int) -> str:
    if hours > 18 or 6 > hours:
        return "The Sun Is Down"
    elif minutes >= 60 or hours >= 24:
        return "Error, Invalid Input"
    else:
        dict[hours] = minutes
        angle_by_hour = (hours - 6) * 15
        angle_by_minutes = (minutes) * 0.25
        return f"Time = {dict}, Angle Of The Sun = {angle_by_hour+angle_by_minutes}"


def sun(time: str) -> str:
    time = input("Enter a time using the military format and a comma (Example: 12:45)")
    time.split(":")
    list.append(time)



print(sun2(7, 00))
