def change_pi(s):
    """
    Given a string, compute recursively a new string where all appearances
    of "pi" have been replaced by "3.14".


    change_pi("xpix") → "x3.14x"
    change_pi("pipi") → "3.143.14"
    change_pi("pip") → "3.14p"
    """

    if len(s) < 2:
        return s

    if s[0:2] == "pi":
        return "3.14" + change_pi(s[2:])

    return s[0] + change_pi(s[1:])


print(change_pi("xpix"))
print(change_pi("pipi"))
print(change_pi("pip"))
