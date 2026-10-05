def has_77(nums):
    """
    Given an array of ints, return true if the array contains two 7's
    next to each other, or there are two 7's separated by one element.

    has_77([1, 7, 7]) → True
    has_77([1, 7, 1, 7]) → True
    has_77([1, 7, 1, 1, 7]) → False
    """

    for i in range(len(nums) - 1):
        if nums[i] == 7 and nums[i + 1] == 7:
            return True

        if i < len(nums) - 2 and nums[i] == 7 and nums[i + 2] == 7:
            return True

    return False


print(has_77([1, 7, 7]))
print(has_77([1, 7, 1, 7]))
print(has_77([1, 7, 1, 1, 7]))
