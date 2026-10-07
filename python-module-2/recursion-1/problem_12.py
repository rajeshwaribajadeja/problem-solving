def change_xy(s):
    """
    Given a string, compute recursively a new string where all
    lowercase 'x' chars have been changed to 'y' chars.


    change_xy("codex") → "codey"
    change_xy("xxhixx") → "yyhiyy"
    change_xy("xhixhix") → "yhiyhiy"
    """

    if s == "":
        return ""

    if s[0] == "x":
        return "y" + change_xy(s[1:])

    return s[0] + change_xy(s[1:])


print(change_xy("codex"))
print(change_xy("xxhixx"))
print(change_xy("xhixhix"))
