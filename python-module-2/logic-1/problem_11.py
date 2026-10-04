def two_as_one(a, b, c):
    """
    Given three ints, a, b, c, return true if it is possible to add
    two of the ints to get the third.

    two_as_one(1, 2, 3) → True
    two_as_one(3, 1, 2) → True
    two_as_one(3, 2, 2) → False
    """

    return a + b == c or a + c == b or b + c == a


print(two_as_one(1, 2, 3))
print(two_as_one(3, 1, 2))
print(two_as_one(3, 2, 2))