def endup(str):
    """
    Given a string, return a new string where the last 3 chars are now in upper case. If the string has less than 3 chars, uppercase whatever is there.

    endup("Hello") → "HeLLO"
    endup("hi there") → "hi thERE"
    endup("hi") → "HI"
    """

    return str[:-3] + str[-3:].upper()

print(endup("Hello"))
print(endup("hi there"))
print(endup("hi"))