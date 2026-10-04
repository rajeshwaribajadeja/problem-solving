def zip_zap(str):
    """
    Look for patterns like "zip" and "zap" in the string -- length-3, starting with 'z' and ending with 'p'. Return a string where for all such words, the middle letter is gone, so "zipXzap" yields "zpXzp".


    zip_zap("zipXzap") → "zpXzp"
    zip_zap("zopzop") → "zpzp"
    zip_zap("zzzopzop") → "zzzpzp" 
    """
    result = ""
    i = 0

    while i < len(str):
        if i + 2 < len(str) and str[i] == 'z' and str[i + 2] == 'p':
            result += "zp"
            i += 3
        else:
            result += str[i]
            i += 1

    return result

print(zip_zap("zipXzap"))
print(zip_zap("zopzop"))
print(zip_zap("zzzopzop"))
