# a = 5
# def test():
#     return a + 3


# sun(time), time: "06:00", "11:30",
# return an angle-str  ,
# "06:00"-0, "12:00"- 90, "18:00"-180,
dict = {}


def sun(time: str) -> str:
    subtracting_number = 600
    if time < 601 or time > 1800:
        return f"Time = {time}, Angle = {0}"
    else:
        while time > subtracting_number:
            divisor = 4
            angle = (time - subtracting_number) / divisor
            subtracting_number += 100
            if time - subtracting_number >
            angle += 15
        return f"Time = {time}, Angle = {angle}"


print(sun(1000))
