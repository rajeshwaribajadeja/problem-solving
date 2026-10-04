def near_ten(num):
    """
    Given a non-negative number "num", return true if num is within
    2 of a multiple of 10.

    near_ten(12) → True
    near_ten(17) → False
    near_ten(19) → True
    """

    remainder = num % 10

    return remainder <= 2 or remainder >= 8


print(near_ten(12))
print(near_ten(17))
print(near_ten(19))