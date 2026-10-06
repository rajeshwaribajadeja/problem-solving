def words_without_list(words, length):
    """
    Given an array of strings, return a new list where all the strings
    of the given length are omitted.


    words_without_list(["a", "bb", "b", "ccc"], 1) → ["bb", "ccc"]
    words_without_list(["a", "bb", "b", "ccc"], 3) → ["a", "bb", "b"]
    words_without_list(["a", "bb", "b", "ccc"], 4) → ["a", "bb", "b", "ccc"]
    """

    result = []

    for word in words:
        if len(word) != length:
            result.append(word)

    return result


print(words_without_list(["a", "bb", "b", "ccc"], 1))
print(words_without_list(["a", "bb", "b", "ccc"], 3))
print(words_without_list(["a", "bb", "b", "ccc"], 4))