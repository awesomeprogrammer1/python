# sun(time), time: "06:00", "11:30",
# return an angle-str  ,
# "06:00"-0, "12:00"- 90, "18:00"-180,


def get_angle(hours: int, minutes: int) -> str:
    if (hours >= 18 and minutes > 0) or (hours <= 5 and minutes <= 59):
        return "The Sun Is Down"
    else:
        angle_by_hour = (hours - 6) * 15
        angle_by_minutes = (minutes) * 0.25
        return f"Angle Of The Sun = {angle_by_hour+angle_by_minutes}"


def sun(time: str) -> str:
    hours_and_minutes = time.split(":")
    try:
        hours_and_minutes = time.split(":")
        hours = int(hours_and_minutes[0])
    except ValueError:
        return "Error, Invalid Input"    
    if minutes <= -1 or hours <= -1:
        return "Error, Invalid Input"
    if minutes >= 60 or hours >= 24:
        return "Error, Invalid Input"
    angle = get_angle(hours, minutes)
    return f"Time = {time}, {angle}"


# only run the commands in the if when you are executing this file
if __name__ == "__main__":
    print(sun("abc"))
