def two_char(str, i):
    """
    Given a string and an index, return a string length 2 starting at the given index. If the index is too big or too small to define a string length 2, use the first 2 chars. The string length will be at least 2.


    two_char("java", 0) → "ja"
    two_char("java", 2) → "va"
    two_char("java", 3) → "ja"
    """
    if 0 <= i <= len(str) - 2:
        return str[i:i+2]
    return str[:2]

print(two_char("java", 0))
print(two_char("java", 2))
print(two_char("java", 3))