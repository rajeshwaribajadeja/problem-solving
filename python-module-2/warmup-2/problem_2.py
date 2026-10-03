def doublex(str):
    """
    Given a string, return true if the first instance of "x" in the string is immediately followed by another "x".

    doublex("axxbb") → true
    doublex("axaxax") → false
    doublex("xxxxx") → true
    """
    # i = str.find("x")    
    # return i != -1 and i + 1 < len(str) and str[i + 1] == "x"

    for i in range(len(str)-1):
        if str[i] == str[i+1] == "x":
            return True

    return False

print(doublex("axxbb"))
print(doublex("axaxax"))
print(doublex("xxxxx"))

