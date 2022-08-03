# assignment 1 for 2022-08-03
# create a function which takes parameter {"width": 50, "height": 70} and
# returns a string that shows area and perimeter


def get_formatted_perimeter_area(dict):
    area = dict["width"] * dict["height"]
    perimeter = (dict["width"] + dict["height"]) * 2
    return f"Perimeter = {perimeter}, Area = {area}"


if __name__ == "__main__":
    dict = {"width": 50, "height": 70}
    print(get_formatted_perimeter_area(dict))
