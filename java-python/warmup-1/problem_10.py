def del_del(str):
    """
    Given a string, if the string "del" appears starting at index 1, return a string where that "del" has been deleted. Otherwise, return the string unchanged.


    del_del("adelbc") → "abc"
    del_del("adelHello") → "aHello"
    del_del("adedbc") → "adedbc"
    """
    if str[1:4] == "del":
        return str[:1] + str[4:]

    return str
    # return str.replace("del","") # Using string method

print(del_del("adelbc"))
print(del_del("adelHello"))
print(del_del("adedbc"))