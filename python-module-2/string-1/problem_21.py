def without_x(str):
    """
    Given a string, if the first or last chars are 'x', return the string without those 'x' chars, and otherwise return the string unchanged.


    without_x("xHix") → "Hi"
    without_x("xHi") → "Hi"
    without_x("Hxix") → "Hxi"
    """
    if str[:1] == "x":
        str = str[1:]
    
    if str[-1:] == "x":
        str = str[:-1]

    return str

print(without_x("xHix"))
print(without_x("xHi"))
print(without_x("Hxix"))