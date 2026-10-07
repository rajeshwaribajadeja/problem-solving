def count_abc(s):
    """
    Count recursively the total number of "abc" and "aba" substrings
    that appear in the given string.


    count_abc("abc") → 1
    count_abc("abcxxabc") → 2
    count_abc("abaxxaba") → 2
    """

    if len(s) < 3:
        return 0

    # if s[0:3] == "abc" or s[0:3] == "aba":
    #     return 1 + count_abc(s[1:])

    return 1 + count_abc(s[1:]) if s[0:3] == "abc" or s[0:3] == "aba" else count_abc(s[1:])


print(count_abc("abc"))
print(count_abc("abcxxabc"))
print(count_abc("abaxxaba"))
