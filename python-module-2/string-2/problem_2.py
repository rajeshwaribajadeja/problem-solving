def xy_balance(str):
    """
    We'll say that a String is xy-balanced if for all the 'x' chars in the string, there exists a 'y' char somewhere later in the string. So "xxy" is balanced, but "xyx" is not. One 'y' can balance multiple 'x's. Return true if the given string is xy-balanced.


    xy_balance("aaxbby") → true
    xy_balance("aaxbb") → false
    xy_balance("yaaxbb") → false
    """


    for i in range(len(str)):
        if str[i] == "x":
            if "y" not in str[i+1:]:
                return False
    return True    

print(xy_balance("aaxbby"))
print(xy_balance("aaxbb"))
print(xy_balance("yaaxbb"))