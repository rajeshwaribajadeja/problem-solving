def last_digit(a, b, c):
    """
    Given three ints, a, b, c, return true if two or more of them
    have the same rightmost digit. The ints are non-negative.

    last_digit(23, 19, 13) → True
    last_digit(23, 19, 12) → False
    last_digit(23, 19, 3) → True
    """

    return a % 10 == b % 10 or a % 10 == c % 10 or b % 10 == c % 10


print(last_digit(23, 19, 13))
print(last_digit(23, 19, 12))
print(last_digit(23, 19, 3))