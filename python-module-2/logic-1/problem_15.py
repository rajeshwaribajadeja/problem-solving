def less_by_10(a, b, c):
    """
    Given three ints, a, b, c, return true if one of them is
    10 or more less than one of the others.

    less_by_10(1, 7, 11) → True
    less_by_10(1, 7, 10) → False
    less_by_10(11, 1, 7) → True
    """

    return (abs(a - b) >= 10 or
            abs(a - c) >= 10 or
            abs(b - c) >= 10)


print(less_by_10(1, 7, 11))
print(less_by_10(1, 7, 10))
print(less_by_10(11, 1, 7))