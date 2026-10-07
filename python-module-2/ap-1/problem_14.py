def words_without(words, target):
    """
    Given an array of strings, return a new array without the strings that are equal to the target string. One approach is to count the occurrences of the target string, make a new array of the correct length, and then copy over the correct strings.


    words_without(["a", "b", "c", "a"], "a") → ["b", "c"]
    words_without(["a", "b", "c", "a"], "b") → ["a", "c", "a"]
    words_without(["a", "b", "c", "a"], "c") → ["a", "b", "a"]
    """

    result = []

    for word in words:
        if word != target:
            result.append(word)

    return result


print(words_without(["a", "b", "c", "a"], "a"))
print(words_without(["a", "b", "c", "a"], "b"))
print(words_without(["a", "b", "c", "a"], "c"))