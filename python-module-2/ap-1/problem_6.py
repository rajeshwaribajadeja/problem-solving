def words_front(words, n):
    """
    Given an array of strings, return a new array containing the first N strings. N will be in the range 1..length


    words_front(["a", "b", "c", "d"], 1) → ["a"]
    words_front(["a", "b", "c", "d"], 2) → ["a", "b"]
    words_front(["a", "b", "c", "d"], 3) → ["a", "b", "c"]
    """

    result = []

    for i in range(n):
        result.append(words[i])

    return result


print(words_front(["a", "b", "c", "d"], 1))
print(words_front(["a", "b", "c", "d"], 2))
print(words_front(["a", "b", "c", "d"], 3))