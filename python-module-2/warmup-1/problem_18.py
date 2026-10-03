def last_digit(a, b):
    """
    Given two non-negative int values, return true if they have the same last digit, such as with 27 and 57. 

    last_digit(7, 17) → true
    last_digit(6, 17) → false
    last_digit(3, 113) → true
    """

    return a % 10 == b % 10

print(last_digit(7, 17))
print(last_digit(6, 17))
print(last_digit(3, 113))