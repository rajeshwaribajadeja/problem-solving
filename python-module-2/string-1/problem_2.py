def theend(str, front):
    """
    Given a string, return a string length 1 from its front, unless front is false, in which case return a string length 1 from its back. The string will be non-empty.


    theend("Hello", true) → "H"
    theend("Hello", false) → "o"
    theend("oh", true) → "o"
    """
    return str[0] if front else str[-1]

print(theend("Hello", True))
print(theend("Hello", False))
print(theend("oh", True))