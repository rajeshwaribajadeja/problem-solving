def fizz_array_3(start, end):
    """
    Given start and end numbers, return a new array containing the sequence of integers from start up to but not including end, so start=5 and end=10 yields {5, 6, 7, 8, 9}. The end number will be greater or equal to the start number. Note that a length-0 array is valid.

    fizz_array_3(5, 10) → [5, 6, 7, 8, 9]
    fizz_array_3(11, 18) → [11, 12, 13, 14, 15, 16, 17]
    fizz_array_3(1, 3) → [1, 2]
    """

    nums = []

    for i in range(start, end):
        nums.append(i)

    return nums

    # solution-2
    # return list(range(start, end))


print(fizz_array_3(5, 10))
print(fizz_array_3(11, 18))
print(fizz_array_3(1, 3))
