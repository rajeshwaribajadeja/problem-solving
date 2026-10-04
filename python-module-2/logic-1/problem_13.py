def in_order_equal(a, b, c, equal_ok):
    """
    Given three ints, a, b, c, return true if they are in strict
    increasing order. If equal_ok is true, equality is allowed.

    in_order_equal(2, 5, 11, False) → True
    in_order_equal(5, 7, 6, False) → False
    in_order_equal(5, 5, 7, True) → True
    """

    if equal_ok:
        return a <= b and b <= c
    else:
        return a < b and b < c


print(in_order_equal(2, 5, 11, False))
print(in_order_equal(5, 7, 6, False))
print(in_order_equal(5, 5, 7, True))