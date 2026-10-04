def more20(n):
    """
    Return true if the given non-negative number is 1 or 2 more
    than a multiple of 20.

    more20(20) → False
    more20(21) → True
    more20(22) → True
    """

    return n % 20 == 1 or n % 20 == 2


print(more20(20))
print(more20(21))
print(more20(22))