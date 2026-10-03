def de_front(str):
    """
    Given a string, return a version without the first 2 chars. Except keep the first char if it is 'a' and keep the second char if it is 'b'. The string may be any length. Harder than it looks.


    de_front("Hello") → "llo"
    de_front("java") → "va"
    de_front("away") → "aay"
    """
    result = ""

    if len(str) > 0 and str[0] == "a":
        result += str[0]

    if len(str) > 1 and str[1] == "b":
        result += str[1]

    return result + str[2:]

print(de_front("Hello"))
print(de_front("java"))
print(de_front("away"))