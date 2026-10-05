def first_char(words):
    """
    Given an array of non-empty strings, return a dictionary with a key for
    every different first character seen, with the value of all the strings
    starting with that character appended together in the order they appear
    in the array.


    first_char(["salt", "tea", "soda", "toast"]) → {"s": "saltsoda", "t": "teatoast"}
    first_char(["aa", "bb", "cc", "aAA", "cCC", "d"]) → {"a": "aaaAA", "b": "bb", "c": "cccCC", "d": "d"}
    first_char([]) → {}
    """

    result = {}

    for word in words:
        key = word[0]

        if key in result:
            result[key] = result[key] + word
        else:
            result[key] = word

    return result


print(first_char(["salt", "tea", "soda", "toast"]))
print(first_char(["aa", "bb", "cc", "aAA", "cCC", "d"]))
print(first_char([]))