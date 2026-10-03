def withouend2(str):
    """
    Given a string, return a version without both the first and last char of the string. The string may be any length, including 0.


    withouend2("Hello") → "ell"
    withouend2("abc") → "b"
    withouend2("ab") → ""
    """
    return str[1:-1]

print(withouend2("Hello"))
print(withouend2("abc"))
print(withouend2("ab"))