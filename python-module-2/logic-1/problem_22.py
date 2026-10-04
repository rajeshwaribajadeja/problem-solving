def sum_limit(a, b):
    """
    Given 2 non-negative ints, a and b, return their sum, so long as
    the sum has the same number of digits as a. If the sum has more
    digits than a, just return a without b.

    sum_limit(2, 3) → 5
    sum_limit(8, 3) → 8
    sum_limit(8, 1) → 9
    """

    if len(str(a + b)) > len(str(a)):
        return a

    return a + b


print(sum_limit(2, 3))
print(sum_limit(8, 3))
print(sum_limit(8, 1))