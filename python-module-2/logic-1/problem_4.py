def less20(n):
    """
    Return true if the given non-negative number is 1 or 2 less than a multiple of 20. So for example 38 and 39 return true, but 40 returns false.

    less20(18) → True
    less20(19) → True
    less20(20) → False
    """

    return n % 20 == 18 or n % 20 == 19


print(less20(18))
print(less20(19))
print(less20(20))