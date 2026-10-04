def old35(n):
    """
    Return true if the given non-negative number is a multiple of 3 or 5,
    but not both.

    old35(3) → True
    old35(10) → True
    old35(15) → False
    """

    return (n % 3 == 0) != (n % 5 == 0)


print(old35(3))
print(old35(10))
print(old35(15))