def plus_out(str, word):
    """
    Given a string and a non-empty word string, return a version of the original String where all chars have been replaced by pluses ("+"), except for appearances of the word string which are preserved unchanged.


    plus_out("12xy34", "xy") → "++xy++"
    plus_out("12xy34", "1") → "1+++++"
    plus_out("12xy34xyabcxy", "xy") → "++xy++xy+++xy"
    """

    result = ""
    i = 0

    while i < len(str):
        if str[i:i+len(word)] == word:
            result += word
            i += len(word)
        else:
            result += "+"
            i += 1

    return result

print(plus_out("12xy34", "xy"))
print(plus_out("12xy34", "1"))
print(plus_out("12xy34xyabcxy", "xy"))
