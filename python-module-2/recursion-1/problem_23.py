def count_11(s):
    """
    Given a string, compute recursively the number of "11" substrings.
    The "11" substrings should not overlap.


    count_11("11abc11") → 2
    count_11("abc11x11x11") → 3
    count_11("111") → 1
    """

    if len(s) < 2:
        return 0

    # if s[0:2] == "11":
    #     return 1 + count_11(s[2:])

    return 1 + count_11(s[2:]) if s[0:2] == "11" else count_11(s[1:])


print(count_11("11abc11"))
print(count_11("abc11x11x11"))
print(count_11("111"))
