def teen_sum(a, b):
    """
    Given 2 ints, a and b, return their sum. However, "teen" values
    in the range 13..19 inclusive, are extra lucky. So if either
    value is a teen, just return 19.

    teen_sum(3, 4) → 7
    teen_sum(10, 13) → 19
    teen_sum(13, 2) → 19
    """

    return 19 if 13 <= a <= 19 or 13 <= b <= 19 else a + b


print(teen_sum(3, 4))
print(teen_sum(10, 13))
print(teen_sum(13, 2))