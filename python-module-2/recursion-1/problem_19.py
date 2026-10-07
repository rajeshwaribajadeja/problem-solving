def pair_star(s):
    """
    Given a string, compute recursively a new string where identical
    chars that are adjacent in the original string are separated by "*".

    
    pair_star("hello") → "hel*lo"
    pair_star("xxyy") → "x*xy*y"
    pair_star("aaaa") → "a*a*a*a"
    """

    if len(s) <= 1:
        return s

    if s[0] == s[1]:
        return s[0] + "*" + pair_star(s[1:])

    return s[0] + pair_star(s[1:])


print(pair_star("hello"))
print(pair_star("xxyy"))
print(pair_star("aaaa"))
