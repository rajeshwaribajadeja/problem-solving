def no_yy(words):
    """
    Given a list of strings, return a list where each string has "y"
    added at its end, omitting any resulting strings that contain
    "yy" as a substring anywhere.


    no_yy(["a", "b", "c"]) → ["ay", "by", "cy"]
    no_yy(["a", "b", "cy"]) → ["ay", "by"]
    no_yy(["xx", "ya", "zz"]) → ["xxy", "yay", "zzy"]
    """

    words = list(map(lambda x: x + "y", words))

    return list(filter(lambda x: "yy" not in x, words))


print(no_yy(["a", "b", "c"]))
print(no_yy(["a", "b", "cy"]))
print(no_yy(["xx", "ya", "zz"]))
