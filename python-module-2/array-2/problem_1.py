def lucky13(nums):
    """
    Given an array of ints, return true if the array contains no 1's
    and no 3's.

    lucky13([0, 2, 4]) → True
    lucky13([1, 2, 3]) → False
    lucky13([1, 2, 4]) → False
    """

    return (1 not in nums) and (3 not in nums)

print(lucky13([0, 2, 4]))
print(lucky13([1, 2, 3]))
print(lucky13([1, 2, 4]))
