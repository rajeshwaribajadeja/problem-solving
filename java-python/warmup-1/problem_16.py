def max1020(a, b):
    """
    Given 2 positive int values, return the larger value that is in the range 10..20 inclusive, or return 0 if neither is in that range.


    max1020(11, 19) → 19
    max1020(19, 11) → 19
    max1020(11, 9) → 11
    """

    if a > b and 10 <= a <= 20:
        return a

    elif b > a and 10 <= b <= 20:
        return b

    else:
        return 0

print(max1020(19, 11))
print(max1020(11, 19))
print(max1020(11, 9))