def startOz(str):
    """
    Given a string, return a string made of the first 2 chars (if present), however include first char only if it is 'o' and include the second only if it is 'z', so "ozymandias" yields "oz".


    startOz("ozymandias") → "oz"
    startOz("bzoo") → "z"
    startOz("oxx") → "o"
    """

    result = ""

    if len(str) > 0 and str[0] == "o":
        result += "o"

    if len(str) > 1 and str[1] == "z":
        result += "z"

    return result

print(startOz("ozymandias"))
print(startOz("bzoo"))
print(startOz("oxx"))