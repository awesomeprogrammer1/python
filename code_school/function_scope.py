# a = 5
# def test():
#     return a + 3


# sun(time), time: "06:00", "11:30",
# return an angle-str  ,
# "06:00"-0, "12:00"- 90, "18:00"-180,


def sun2(hours: int, minutes: int) -> str:
    if hours > 18 or 6 > hours:
        return "The Sun Is Down"
    if minutes >= 60 or hours >= 24:
        return "Error, Invalid Input"
    else:
        angle_by_hour = (hours - 6) * 15
        angle_by_minutes = (minutes) * 0.25
        return f"Time = {'7:15'}, Angle Of The Sun = {angle_by_hour + angle_by_minutes}"


def sun(time: str) -> str:
    list = time.split(":")
    hours = int(list[0])
    minutes = int(list[1])
    return sun2(hours, minutes)


print(sun("7:15"))
