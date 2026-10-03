def see_color(str):
    """
    Given a string, if the string begins with "red" or "blue" return that color string, otherwise return the empty string.


    see_color("redxx") → "red"
    see_color("xxred") → ""
    see_color("blueTimes") → "blue"
    """
    if str[:len("red")] == "red":
        return "red"

    elif str[:len("blue")] == "blue":
        return "blue"

    else:
        return ""

    # if str.startswith("red"):
    #     return "red"
    # elif str.startswith("blue"):
    #     return "blue"
    # else:
    #     return ""

print(see_color("redxx"))
print(see_color("xxred"))
print(see_color("blueTimes"))