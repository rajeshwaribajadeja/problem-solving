def middletwo(str):
    """
    Given a string of even length, return a string made of the middle two chars, so the string "string" yields "ri". The string length will be at least 2.


    middletwo("string") → "ri"
    middletwo("code") → "od"
    middletwo("Practice") → "ct"
    """
    return str[len(str)//2-1] + str[len(str)//2]
    
print(middletwo("string"))
print(middletwo("code"))
print(middletwo("Practice"))