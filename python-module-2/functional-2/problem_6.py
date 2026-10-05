def no_34(words):
    """
    Given a list of strings, return a list of the strings,
    omitting any string length 3 or 4.


    no_34(["a", "bb", "ccc"]) → ["a", "bb"]
    no_34(["a", "bb", "ccc", "dddd"]) → ["a", "bb"]
    no_34(["ccc", "dddd", "apple"]) → ["apple"]
    """

    return list(filter(lambda x: len(x) != 3 and len(x) != 4, words))


print(no_34(["a", "bb", "ccc"]))
print(no_34(["a", "bb", "ccc", "dddd"]))
print(no_34(["ccc", "dddd", "apple"]))
