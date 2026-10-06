def words_count(words, length):
    """
    Given an array of strings, return the count of the number of strings
    with the given length.


    words_count(["a", "bb", "b", "ccc"], 1) → 2
    words_count(["a", "bb", "b", "ccc"], 3) → 1
    words_count(["a", "bb", "b", "ccc"], 4) → 0
    """

    count = 0

    for word in words:
        if len(word) == length:
            count += 1

    return count


print(words_count(["a", "bb", "b", "ccc"], 1))
print(words_count(["a", "bb", "b", "ccc"], 3))
print(words_count(["a", "bb", "b", "ccc"], 4))