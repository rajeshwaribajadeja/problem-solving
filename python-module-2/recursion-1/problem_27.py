def nest_paren(s):
    """
    Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside them.


    nest_paren("(())")  → True
    nest_paren("((()))") → True
    nest_paren("(((x))") → False
    """ 

    if s == "":
        return True

    if s[0] == "(" and s[-1] == ")":
        return nest_paren(s[1:-1])

    return False


print(nest_paren("(())"))
print(nest_paren("((()))"))
print(nest_paren("(((x))"))
