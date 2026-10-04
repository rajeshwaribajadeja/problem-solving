def bob_there(str):
    """
    Return true if the given string contains a "bob" string, but where the middle 'o' char can be any char.


    bob_there("abcbob") → true
    bob_there("b9b") → true
    bob_there("bac") → false
    """

    for i in range(len(str)-2):
        return str[i] == str[i+2] =="b"

    return False

print(bob_there("abcbob"))
print(bob_there("b9b"))
print(bob_there("bac"))
             