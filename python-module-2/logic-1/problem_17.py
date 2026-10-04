def max_mod5(a, b):
    """
    Given two int values, return whichever value is larger.
    However, if the two values have the same remainder when divided
    by 5, return the smaller value. If the two values are the same,
    return 0.

    max_mod5(2, 3) → 3
    max_mod5(6, 2) → 6
    max_mod5(3, 2) → 3
    """

    if a == b:
        return 0

    if a % 5 == b % 5:
        return min(a, b)

    return max(a, b)


print(max_mod5(2, 3))
print(max_mod5(6, 2))
print(max_mod5(3, 2))