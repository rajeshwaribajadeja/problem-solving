def word_append(words):
    """
    Loop over the given array of strings to build a result string like this:
    when a string appears the 2nd, 4th, 6th, etc. time in the array, append
    the string to the result. Return the empty string if no string appears
    a 2nd time.


    word_append(["a", "b", "a"]) → "a"
    word_append(["a", "b", "a", "c", "a", "d", "a"]) → "aa"
    word_append(["a", "", "a"]) → "a"
    """

    count = {}
    result = ""

    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1

        if count[word] % 2 == 0:
            result = result + word

    return result


print(word_append(["a", "b", "a"]))
print(word_append(["a", "b", "a", "c", "a", "d", "a"]))
print(word_append(["a", "", "a"]))