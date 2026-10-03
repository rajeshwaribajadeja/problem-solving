def without_x2(str):
    """
    Given a string, if one or both of the first 2 chars is 'x', return the string without those 'x' chars, and otherwise return the string unchanged. This is a little harder than it looks.

    without_x2("xHi") → "Hi"
    without_x2("Hxi") → "Hi"
    without_x2("Hi") → "Hi"
    """
    res = ""

    if str[:1] != "x":
        res += str[:1]

    if str[1:2] != "x":
        res += str[1:2]

    return res + str[2:]

print(without_x2("xHi"))
print(without_x2("Hxi"))
print(without_x2("Hi"))