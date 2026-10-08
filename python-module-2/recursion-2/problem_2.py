def group_sum_6(start, nums, target):
    """
    Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, such that the group sums to the given target? However, with the additional constraint that all 6's must be chosen. (No loops needed.)


    group_sum_6(0, [5, 6, 2], 8) → True
    group_sum_6(0, [5, 6, 2], 9) → False
    group_sum_6(0, [5, 6, 2], 7) → False
    """

    if start == len(nums):
        return target == 0

    if nums[start] == 6:
        return group_sum_6(start + 1, nums, target - 6)

    if group_sum_6(start + 1, nums, target - nums[start]):
        return True

    return group_sum_6(start + 1, nums, target)


print(group_sum_6(0, [5, 6, 2], 8))
print(group_sum_6(0, [5, 6, 2], 9))
print(group_sum_6(0, [5, 6, 2], 7))
