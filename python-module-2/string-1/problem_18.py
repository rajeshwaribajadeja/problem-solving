def without2(str):
    """
    Given a string, if a length 2 substring appears at both its beginning and end, return a string without the substring at the beginning, so "HelloHe" yields "lloHe". The substring may overlap with itself, so "Hi" yields "". Otherwise, return the original string unchanged.


    without2("HelloHe") → "lloHe"
    without2("HelloHi") → "HelloHi"
    without2("Hi") → ""
    """
    return str[2:-2] if str[:2] == str[-2:] else str

print(without2("HelloHe"))
print(without2("HelloHi"))
print(without2("Hi"))