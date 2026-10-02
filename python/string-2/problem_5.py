
def end_other(a, b):
    """
    Given two strings, return True if one of the strings appears at the very end of the other string.
    Return True also if the strings are equal. Case insensitive.
    Note: s.lower() returns the lowercase version of a string.

    end_other('Hiabc', 'abc') → True
    end_other('Abc', 'Hiabc') → True
    end_other('abc', 'abXabc') → True
    """

    a = a.lower()
    b = b.lower()

    # return a.endswith(b) or b.endswith(a)
    return a[-len(b):] == b or b[-len(a):] == a

    

print(end_other('Hiabc', 'abc'))
print(end_other('Abc', 'Hiabc'))
print(end_other('abc', 'abXabc'))
