def only_14(nums):
    """
    Given an array of ints, return true if every element is a 1 or a 4.

    only_14([1, 4, 1, 4]) → True
    only_14([1, 4, 2, 4]) → False
    only_14([1, 1]) → True
    """

    for num in nums:
        if num != 1 and num != 4:
            return False

    return True


print(only_14([1, 4, 1, 4]))
print(only_14([1, 4, 2, 4]))
print(only_14([1, 1]))