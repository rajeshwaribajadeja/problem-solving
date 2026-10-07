def end_x(s):
    """
    Given a string, compute recursively a new string where all the
    lowercase 'x' chars have been moved to the end of the string.


    end_x("xxre") → "rexx"
    end_x("xxhixx") → "hixxxx"
    end_x("xhixhix") → "hihixxx"
    """

    if s == "":
        return ""

    # if s[0] == "x":
    #     return end_x(s[1:]) + "x"

    return end_x(s[1:]) + "x" if s[0] == "x" else s[0] + end_x(s[1:])


print(end_x("xxre"))
print(end_x("xxhixx"))
print(end_x("xhixhix"))
