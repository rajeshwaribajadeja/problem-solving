def sum28(nums):
    """
    Given an array of ints, return true if the sum of all the 2's
    in the array is exactly 8.

    sum28([2, 3, 2, 2, 4, 2]) → True
    sum28([2, 3, 2, 2, 4, 2, 2]) → False
    sum28([1, 2, 3, 4]) → False
    """

    total = 0

    for num in nums:
        if num == 2:
            total += 2

    return total == 8


print(sum28([2, 3, 2, 2, 4, 2]))
print(sum28([2, 3, 2, 2, 4, 2, 2]))
print(sum28([1, 2, 3, 4]))
