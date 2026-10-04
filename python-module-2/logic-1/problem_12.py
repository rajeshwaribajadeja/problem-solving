def in_order(a, b, c, b_ok):
    """
    Given three ints, a, b, c, return true if b is greater than a,
    and c is greater than b. However, if b_ok is true, b does not
    need to be greater than a.

    in_order(1, 2, 4, False) → True
    in_order(1, 2, 1, False) → False
    in_order(1, 1, 2, True) → True
    """

    if b_ok:
        return c > b
    else:
        return b > a and c > b


print(in_order(1, 2, 4, False))
print(in_order(1, 2, 1, False))
print(in_order(1, 1, 2, True))