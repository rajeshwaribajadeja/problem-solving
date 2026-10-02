def pos_neg(a, b, negative):
    """
    Given 2 int values, a and b, return True if one is positive and one is negative (not both positive or both negative). Except if the parameter "negative" is True, then return True only if both are negative.


    pos_neg(1, -1, False) → True
    pos_neg(-1, -1, False) → False
    pos_neg(-4, -5, True) → True
    """
    if negative:
        return a < 0 and b < 0

    return (a < 0 and b > 0) or (a > 0 and b < 0)

print(pos_neg(1, -1, False))
print(pos_neg(-1, -1, False))
print(pos_neg(-4, -5, True))