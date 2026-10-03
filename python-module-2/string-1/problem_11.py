def last_chars(a, b):
    """
    Given 2 strings, a and b, return a new string made of the first char of a and the last char of b, so "yo" and "java" yields "ya". If either string is length 0, use '@' for its missing char.


    last_chars("last", "chars") → "ls"
    last_chars("yo", "java") → "ya"
    last_chars("hi", "") → "h@"
    """
    return (a[0] if a else "@") + (b[-1] if b else "@")

print(last_chars("last", "chars"))
print(last_chars("yo", "java"))
print(last_chars("hi", ""))