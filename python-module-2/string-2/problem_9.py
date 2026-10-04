def get_sandwich(str):
    """
    A sandwich is two pieces of bread with something in between. Return the string that is between the first and last appearance of "bread" in the given string, or return the empty string "" if there are not two pieces of bread.


    get_sandwich("breadjambread") → "jam"
    get_sandwich("xxbreadjambreadyy") → "jam"
    get_sandwich("xxbreadyy") → ""
    """
    if str.count("bread") < 2:
        return ""

    first = -1
    last = -1
    for i in range(len(str) - 4):
        if str[i:i + 5] == "bread":
            if first == -1:
                first = i
            last = i

    return str[first + 5 : last]

print(get_sandwich("breadjambread"))
print(get_sandwich("xxbreadjambreadyy"))
print(get_sandwich("xxbreadyy"))
    
    