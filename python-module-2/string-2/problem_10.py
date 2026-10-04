def same_star_char(str):
    """
    Returns true if for every '*' (star) in the string, if there are chars both immediately before and after the star, they are the same.


    same_star_char("xy*yzz") → true
    same_star_char("xy*zzz") → false
    same_star_char("*xa*az") → true
    """
    for i in range(1, len(str) - 1):
        if str[i] == "*":
            if str[i - 1] != str[i + 1]:
                return False
    return True

print(same_star_char("xy*yzz"))
print(same_star_char("xy*zzz"))
print(same_star_char("*xa*az"))
