def middle_three(str):
    """
    Given a string of odd length, return the string length 3 from its middle, so "Candy" yields "and". The string length will be at least 3.


    middle_three("Candy") → "and"
    middle_three("and") → "and"
    middle_three("solving") → "lvi"
    """
    return str[len(str)//2-1] + str[len(str)//2] + str[len(str)//2+1]

print(middle_three("Candy"))
print(middle_three("and"))
print(middle_three("solving"))