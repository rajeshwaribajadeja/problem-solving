def all_star(s):
    """
    Given a string, compute recursively a new string where all
    the adjacent chars are now separated by a "*".


    all_star("hello") → "h*e*l*l*o"
    all_star("abc") → "a*b*c"
    all_star("ab") → "a*b"
    """

    if len(s) <= 1:
        return s

    # return s[0] + "*" + all_star(s[1:])

    return s[0] + "*" + all_star(s[1:]) if len(s) > 1 else s


print(all_star("hello"))
print(all_star("abc"))
print(all_star("ab"))
