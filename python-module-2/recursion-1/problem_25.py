def count_hi_2(s):
    """
    Given a string, compute recursively the number of times lowercase
    "hi" appears in the string, but do not count "hi" that have an
    "x" immediately before them.


    count_hi_2("ahixhi") → 1
    count_hi_2("ahibhi") → 2
    count_hi_2("xhixhi") → 0
    """

    if len(s) < 2:
        return 0

    if s[0:2] == "hi":
        return 1 + count_hi_2(s[2:])

    if len(s) >= 3 and s[0] == "x" and s[1:3] == "hi":
        return count_hi_2(s[3:])

    return count_hi_2(s[1:])


print(count_hi_2("ahixhi"))
print(count_hi_2("ahibhi"))
print(count_hi_2("xhixhi"))
