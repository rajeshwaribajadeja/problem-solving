def paren_bit(s):
    """
    Given a string that contains a single pair of parenthesis, compute
    recursively a new string made only of the parenthesis and their contents.


    paren_bit("xyz(abc)123") → "(abc)"
    paren_bit("x(hello)") → "(hello)"
    paren_bit("(xy)1") → "(xy)"
    """

    if s[0] == "(":
        return s[:s.index(")") + 1]

    return paren_bit(s[1:])


print(paren_bit("xyz(abc)123"))
print(paren_bit("x(hello)"))
print(paren_bit("(xy)1"))
