def same_ends(str):
    """
    Given a string, return the longest substring that appears at both
    the beginning and end of the string without overlapping.

    same_ends("abXYab") → "ab"
    same_ends("xx") → "x"
    same_ends("xxx") → "x"
    """

    longest = ""

    for i in range(1, len(str) // 2 + 1):
        if str[:i] == str[-i:]:
            longest = str[:i]

    return longest


print(same_ends("abXYab"))
print(same_ends("xx"))
print(same_ends("xxx"))
