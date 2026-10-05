def word_len(words):
    """
    Given an array of strings, return a dictionary containing a key for every
    different string in the array, and the value is that string's length.


    word_len(["a", "bb", "a", "bb"]) → {"bb": 2, "a": 1}
    word_len(["this", "and", "that", "and"]) → {"that": 4, "and": 3, "this": 4}
    word_len(["code", "code", "code", "bug"]) → {"code": 4, "bug": 3}
    """

    result = {}

    for word in words:
        result[word] = len(word)

    return result


print(word_len(["a", "bb", "a", "bb"]))
print(word_len(["this", "and", "that", "and"]))
print(word_len(["code", "code", "code", "bug"]))