def copy_evens(nums, count):
    """
    Given an array of positive ints, return a new array of length "count" containing the first even numbers from the original array. The original array will contain at least "count" even numbers.


    copy_evens([3, 2, 4, 5, 8], 2) → [2, 4]
    copy_evens([3, 2, 4, 5, 8], 3) → [2, 4, 8]
    copy_evens([6, 1, 2, 4, 5, 8], 3) → [6, 2, 4]
    """

    result = []

    for num in nums:
        if num % 2 == 0:
            result.append(num)

            if len(result) == count:
                break

    return result


print(copy_evens([3, 2, 4, 5, 8], 2))
print(copy_evens([3, 2, 4, 5, 8], 3))
print(copy_evens([6, 1, 2, 4, 5, 8], 3))