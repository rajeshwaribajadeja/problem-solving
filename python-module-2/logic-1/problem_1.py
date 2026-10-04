def special_eleven(n):
    """
    We'll say a number is special if it is a multiple of 11 or if it is
    one more than a multiple of 11. Return true if the given non-negative
    number is special.

    special_eleven(22) → True
    special_eleven(23) → True
    special_eleven(24) → False
    """

    return n % 11 == 0 or n % 11 == 1


print(special_eleven(22))
print(special_eleven(23))
print(special_eleven(24))