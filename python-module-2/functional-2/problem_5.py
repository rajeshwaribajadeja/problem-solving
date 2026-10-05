def no_long(words):
    """
    Given a list of strings, return a list of the strings,
    omitting any string length 4 or more.


    no_long(["this", "not", "too", "long"]) → ["not", "too"]
    no_long(["a", "bbb", "cccc"]) → ["a", "bbb"]
    no_long(["cccc", "cccc", "cccc"]) → []
    """

    return list(filter(lambda x: len(x) < 4, words))


print(no_long(["this", "not", "too", "long"]))
print(no_long(["a", "bbb", "cccc"]))
print(no_long(["cccc", "cccc", "cccc"]))
