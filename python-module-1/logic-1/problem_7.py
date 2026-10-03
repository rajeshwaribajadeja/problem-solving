def love6(a, b):
    """
    Given 2 int values, a and b, return True if either of them is 6. Or if their sum or difference is 6.
    Note: the abs() function makes the absolute value of a number.
    
    love6(6, 4) → True
    love6(4, 5) → False
    love6(1, 5) → True
    """

    return a == 6 or b == 6 or abs(a - b) == 6 or a + b == 6

print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))
