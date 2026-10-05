def no_z(words):
    """
    Given a list of strings, return a list of the strings,
    omitting any string that contains a "z".


    no_z(["aaa", "bbb", "aza"]) → ["aaa", "bbb"]
    no_z(["hziz", "hzello", "hi"]) → ["hi"]
    no_z(["hello", "howz", "are", "youz"]) → ["hello", "are"]
    """

    return list(filter(lambda x: "z" not in x, words))


print(no_z(["aaa", "bbb", "aza"]))
print(no_z(["hziz", "hzello", "hi"]))
print(no_z(["hello", "howz", "are", "youz"]))
