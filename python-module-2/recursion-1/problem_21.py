def count_pairs(s):
    """
    We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in the given string.


    count_pairs("axa") → 1
    count_pairs("axax") → 2
    count_pairs("axbx") → 1
    """

    if len(s) < 3:
        return 0

    # if s[0] == s[2]:
    #     return 1 + count_pairs(s[1:])

    return 1 + count_pairs(s[1:]) if s[0] == s[2] else count_pairs(s[1:])


print(count_pairs("axa"))
print(count_pairs("axax"))
print(count_pairs("axbx"))
