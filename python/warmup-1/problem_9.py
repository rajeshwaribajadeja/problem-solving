
def not_string(str):
    """
    Given a string, take the result of putting 'not ' in front of the string. 
    Return this 'not' added result, unless the string begins with 'not' already, 
    in which case return the string unchanged.


    not_string('candy') → 'not candy'
    not_string('x') → 'not x'
    not_string('not bad') → 'not bad'
    """
    return str if len(str) >= 3 and str[:3] == "not" else "not " + str # using string slicing

    # return "not " + str if not str.startswith('not') else str # using string method


print(not_string('candy'))
print(not_string('x'))
print(not_string('not bad'))

