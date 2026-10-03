def extra_front(str):
    """
    Given a string, return a new string made of 3 copies of the first 2 chars of the original string. The string may be any length. If there are fewer than 2 chars, use whatever is there.

    extra_front("Hello") → "HeHeHe"
    extra_front("ab") → "ababab"
    extra_front("H") → "HHH"
    """
    return str[:2] * 3

print(extra_front("Hello"))
print(extra_front("ab"))
print(extra_front("H"))