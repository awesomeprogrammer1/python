# assignment 2 for 2022-08-03
# implement function sun
# sun(time), time: "06:00", "11:30",
# return an angle-str  ,
# "06:00"-0, "12:00"- 90, "18:00"-180,


def get_angle(hours: int, minutes: int) -> str:
    # checks to make sure that the sun isnt down
    # if the sun is down, it returns the string
    # "The Sun is Down"
    # Otherwise, it runs a program which calculates
    # the angle of the sun, dependant on the parameters
    # given to the program by the user
    # the data is then returned to the main program sun
    if (hours >= 18 and minutes > 0) or (hours <= 5 and minutes <= 59):
        return "The Sun Is Down"
    else:
        angle_by_hour = (hours - 6) * 15
        angle_by_minutes = (minutes) * 0.25
        return f"Angle Of The Sun = {angle_by_hour+angle_by_minutes}"


def sun(time: str) -> str:
    # splits the characters in the string by a colon
    hours_and_minutes = time.split(":")
    try:
        # splits the characters in the string by a colon
        hours_and_minutes = time.split(":")
        # converts "hours" from a string to an integer
        hours = int(hours_and_minutes[0])
        # converts "minutes" from a string to an integer
        minutes = int(hours_and_minutes[1])
    # If there is a typeError or a ValueError this message is returned
    except (TypeError, ValueError):
        return "Error, Invalid Input"
    # Checks if the numbers are negative
    if minutes <= -1 or hours <= -1:
        return "Error, Invalid Input"
    # checks if minutes is equal to or over 60
    # and does the same thing with hours
    # if either condition holds true
    # the program raises an exception
    if minutes >= 60 or hours >= 24:
        return "Error, Invalid Input"
    # gets the angle with the help of the other function
    angle = get_angle(hours, minutes)
    # returns the formatted string
    return f"Time = {time}, {angle}"


# only run the commands in the if when you are executing this file
if __name__ == "__main__":
    print(sun("abc"))
