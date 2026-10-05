def word_count(words):
    """
    Given an array of strings, return a dictionary with a key for each
    different string, with the value being the number of times that
    string appears in the array.


    word_count(["a", "b", "a", "c", "b"]) → {"a": 2, "b": 2, "c": 1}
    word_count(["c", "b", "a"]) → {"a": 1, "b": 1, "c": 1}
    word_count(["c", "c", "c", "c"]) → {"c": 4}
    """

    result = {}

    for word in words:
        if word in result:
            result[word] = result[word] + 1
        else:
            result[word] = 1

    return result


print(word_count(["a", "b", "a", "c", "b"]))
print(word_count(["c", "b", "a"]))
print(word_count(["c", "c", "c", "c"]))