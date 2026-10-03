def stringx(str):
    """
    Given a string, return a version where all the "x" have been removed. Except an "x" at the very start or end should not be removed.


    stringx("xxHxix") → "xHix"
    stringx("abxxxcd") → "abcd"
    stringx("xabxxxcdx") → "xabcdx"
    """
    result = ""

    for i in range(len(str)):
        if str[i] != "x" or i == 0 or i == len(str) - 1:
            result += str[i]

    return result

print(stringx("xxHxix"))
print(stringx("abxxxcd"))
print(stringx("xabxxxcdx"))