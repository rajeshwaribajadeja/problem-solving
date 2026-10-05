def no_14(nums):
    """
    Given an array of ints, return true if it contains no 1's
    or it contains no 4's.

    no_14([1, 2, 3]) → True
    no_14([1, 2, 3, 4]) → False
    no_14([2, 3, 4]) → True
    """

    return (1 not in nums) or (4 not in nums)


print(no_14([1, 2, 3]))
print(no_14([1, 2, 3, 4]))
print(no_14([2, 3, 4]))
