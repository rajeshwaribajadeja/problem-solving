def fix23(nums):
    """
    Given an int array length 3, if there is a 2 in the array immediately
    followed by a 3, set the 3 element to 0. Return the changed array.

    fix23([1, 2, 3]) → [1, 2, 0]
    fix23([2, 3, 5]) → [2, 0, 5]
    fix23([1, 2, 1]) → [1, 2, 1]
    """

    if nums[0] == 2 and nums[1] == 3:
        nums[1] = 0

    if nums[1] == 2 and nums[2] == 3:
        nums[2] = 0

    return nums

    # for i in range(len(nums) - 1):
    #     if nums[i] == 2 and nums[i + 1] == 3:
    #         nums[i + 1] = 0

    # return nums



print(fix23([1, 2, 3]))
print(fix23([2, 3, 5]))
print(fix23([1, 2, 1]))
