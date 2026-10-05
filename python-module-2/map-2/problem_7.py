def word_multiple(words):
    """
    Given an array of strings, return a dictionary where each different
    string is a key and its value is True if that string appears 2 or
    more times in the array.


    word_multiple(["a", "b", "a", "c", "b"]) → {"a": True, "b": True, "c": False}
    word_multiple(["c", "b", "a"]) → {"a": False, "b": False, "c": False}
    word_multiple(["c", "c", "c", "c"]) → {"c": True}
    """

    result = {}

    for word in words:
        if word in result:
            result[word] = True
        else:
            result[word] = False

    return result


print(word_multiple(["a", "b", "a", "c", "b"]))
print(word_multiple(["c", "b", "a"]))
print(word_multiple(["c", "c", "c", "c"]))