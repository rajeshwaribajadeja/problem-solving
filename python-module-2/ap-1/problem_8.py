def has_one(n):
    """
    Given a positive int n, return True if it contains a 1 digit.


    has_one(10) → True
    has_one(22) → False
    has_one(220) → False
    """

    while n > 0:
        if n % 10 == 1:
            return True

        n = n // 10

    return False


print(has_one(10))
print(has_one(22))
print(has_one(220))