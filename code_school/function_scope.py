# a = 5
# def test():
#     return a + 3


# sun(time), time: "06:00", "11:30",
# return an angle-str  ,
# "06:00"-0, "12:00"- 90, "18:00"-180,
dict = {}


def sun(time: str) -> str:
    angle = time / 3.75
    if time < 601 or time > 1800:
        return f"Time = {time}, Angle = {0}"
    else:
        while True:
            divisor = 4
            angle = (time - 600) / divisor
            return f"Time = {time}, Angle = {angle}"



print(sun(700))
