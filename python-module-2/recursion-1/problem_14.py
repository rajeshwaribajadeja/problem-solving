def no_x(s):
    """
    Given a string, compute recursively a new string where all
    the 'x' chars have been removed.


    no_x("xaxb") → "ab"
    no_x("abc") → "abc"
    no_x("xx") → ""
    """

    if s == "":
        return ""

    # if s[0] == "x":
    #     return no_x(s[1:])

    return no_x(s[1:]) if s[0] == "x" else s[0] + no_x(s[1:])


print(no_x("xaxb"))
print(no_x("abc"))
print(no_x("xx"))
