def front_again(str):
    """
    Given a string, return true if the first 2 chars in the string also appear at the end of the string, such as with "edited".


    front_again("edited") → true
    front_again("edit") → false
    front_again("ed") → true
    """

    return str[:2] == str[-2:]

print(front_again("edited"))
print(front_again("edit"))
print(front_again("ed"))