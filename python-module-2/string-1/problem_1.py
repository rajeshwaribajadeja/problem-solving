def right2(str):
    """
    Given a string, return a "rotated right 2" version where the last 2 chars are moved to the start. The string length will be at least 2.


    right2("Hello") → "loHel"
    right2("java") → "vaja"
    right2("Hi") → "Hi"
    """
    return str[-2:] + str[:-2]

print(right2("Hello"))
print(right2("java"))
print(right2("Hi"))