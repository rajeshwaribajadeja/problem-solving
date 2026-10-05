def factorial(n):
    """
    Given n of 1 or more, return the factorial of n.
    Compute the result recursively (without loops).


    factorial(1) → 1
    factorial(2) → 2
    factorial(3) → 6
    """

    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(1))
print(factorial(2))
print(factorial(3))
