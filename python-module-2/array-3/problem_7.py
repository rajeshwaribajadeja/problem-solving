def series_up(n):
    """
    Given n>=0, create an array with the pattern {1,    1, 2,    1, 2, 3,   ... 1, 2, 3 .. n} (spaces added to show the grouping). Note that the length of the array will be 1 + 2 + 3 ... + n, which is known to sum to exactly n*(n + 1)/2.


    series_up(3) → [1, 1, 2, 1, 2, 3]
    series_up(4) → [1, 1, 2, 1, 2, 3, 1, 2, 3, 4]
    series_up(2) → [1, 1, 2]
    """

    result = []

    for i in range(1, n + 1):
        result += range(1, i + 1)

    return result


print(series_up(3))
print(series_up(4))
print(series_up(2))
