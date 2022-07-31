# a = 5
# def test():
#     return a + 3


# sun(time), time: "06:00", "11:30",
# return an angle-str  ,
# "06:00"-0, "12:00"- 90, "18:00"-180,
dict = {}


def sun(hours: int, minutes: int) -> str:
    if hours > 18 or 6 > hours:
        return "The Sun Is Down"
    elif minutes >= 60 or hours >= 24:
        return "Error, Invalid Input"
    if minutes == 00:
        dict[hours] = '00'
        angle_by_hour = (hours - 6) * 15
        angle_by_minutes = (minutes) * 0.25
        return f"Time = {dict}, Angle Of The Sun = {angle_by_hour+angle_by_minutes}"
    else:
        dict[hours] = minutes
        angle_by_hour = (hours - 6) * 15
        angle_by_minutes = (minutes) * 0.25
        return f"Time = {dict}, Angle Of The Sun = {angle_by_hour+angle_by_minutes}"


print(sun(7, 00))
