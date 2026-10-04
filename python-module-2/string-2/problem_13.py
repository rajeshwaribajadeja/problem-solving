def star_out(str):
    """
    Return a version of the given string, where for every star (*) in the string the star and the chars immediately to its left and right are gone. So "ab*cd" yields "ad" and "ab**cd" also yields "ad".


    star_out("ab*cd") → "ad"
    star_out("ab**cd") → "ad"
    star_out("sm*eilly") → "silly"
    """

    result = ""
    for i in range(len(str)):
        if str[i] == '*':
            continue
        if i > 0 and str[i - 1] == '*':
            continue
        if i < len(str) - 1 and str[i + 1] == '*':
            continue

        result += str[i]

    return result

print(star_out("ab*cd"))
print(star_out("ab**cd"))
print(star_out("sm*eilly"))
