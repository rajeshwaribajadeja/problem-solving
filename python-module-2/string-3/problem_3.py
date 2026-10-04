def equal_is_not(str):
    """
    Given a string, return true if the number of appearances of "is" anywhere in the string is equal to the number of appearances of "not" anywhere in the string (case sensitive).


    equal_is_not("This is not") → false
    equal_is_not("This is notnot") → true
    equal_is_not("noisxxnotyynotxisi") → true
    """
    is_count = 0
    not_count = 0
    for i in range(len(str)):
        if i + 2 <= len(str) and str[i:i+2] == "is":
            is_count += 1
        if i + 3 <= len(str) and str[i:i+3] == "not":
            not_count += 1
    return is_count == not_count

print(equal_is_not("This is not"))
print(equal_is_not("This is notnot"))
print(equal_is_not("noisxxnotyynotxisi"))
