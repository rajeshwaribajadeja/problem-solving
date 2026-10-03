def at_first(str):
    """
    Given a string, return a string length 2 made of its first 2 chars. If the string length is less than 2, use '@' for the missing chars.


    at_first("hello") → "he"
    at_first("hi") → "hi"
    at_first("h") → "h@"
    """
    if len(str) < 2:
        return str + (2 - len(str)) * "@"

    return str[:2]

print(at_first("hello"))
print(at_first("hi"))
print(at_first("h"))