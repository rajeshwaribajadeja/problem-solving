def string_yak(str):
    """
    Suppose the string "yak" is unlucky. Given a string, return a version where all the "yak" are removed, but the "a" can be any char. The "yak" strings will not overlap.


    string_yak("yakpak") → "pak"
    string_yak("pakyak") → "pak"
    string_yak("yak123ya") → "123ya"
    """

    result = ""
    i = 0
    
    while i < len(str):
        if i + 2 < len(str) and str[i] == "y" and str[i + 2] == "k":            
            i += 3

        else:
            result += str[i]
            i += 1

    return result

print(string_yak("yakpak"))
print(string_yak("pakyak"))
print(string_yak("yak123ya"))