def double23(nums):
    """
    Given an int array, return true if the array contains 2 twice,
    or 3 twice. The array will be length 0, 1, or 2.

    double23([2, 2]) → True
    double23([3, 3]) → True
    double23([2, 3]) → False
    """

    return nums == [2, 2] or nums == [3, 3]


print(double23([2, 2]))
print(double23([3, 3]))
print(double23([2, 3]))

