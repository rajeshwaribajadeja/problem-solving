
def not_replace(str):
    """
    Given a string, return a string where every appearance of the lowercase
    word "is" has been replaced with "is not".

    not_replace("is test") → "is not test"
    not_replace("is-is") → "is not-is not"
    not_replace("This is right") → "This is not right"
    """

    result = ""
    i = 0

    while i < len(str):
        if (str[i:i + 2] == "is" and
            (i == 0 or not str[i - 1].isalpha()) and
            (i + 2 == len(str) or not str[i + 2].isalpha())):

            result += "is not"
            i += 2
        else:
            result += str[i]
            i += 1

    return result


print(not_replace("is test"))
print(not_replace("is-is"))
print(not_replace("This is right"))