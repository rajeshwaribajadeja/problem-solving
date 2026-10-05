def count_7(n):
    """
    Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).


    count_7(717) → 2
    count_7(7) → 1
    count_7(123) → 0
    """

    if n == 0:
        return 0

    if n % 10 == 7:
        return 1 + count_7(n // 10)

    return count_7(n // 10)


print(count_7(717))
print(count_7(7))
print(count_7(123))
