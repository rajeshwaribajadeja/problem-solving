def group_sum_5(start, nums, target):
    """
    Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with these additional constraints: all multiples of 5 in the array must be included in the group. If the value immediately following a multiple of 5 is 1, it must not be chosen. (No loops needed.)

    group_sum_5(0, [2, 5, 10, 4], 19) → True
    group_sum_5(0, [2, 5, 10, 4], 17) → True
    group_sum_5(0, [2, 5, 10, 4], 12) → False
    """

    if start == len(nums):
        return target == 0

    if nums[start] % 5 == 0:
        if start + 1 < len(nums) and nums[start + 1] == 1:
            return group_sum_5(start + 2, nums, target - nums[start])

        return group_sum_5(start + 1, nums, target - nums[start])

    if group_sum_5(start + 1, nums, target - nums[start]):
        return True

    return group_sum_5(start + 1, nums, target)


print(group_sum_5(0, [2, 5, 10, 4], 19))
print(group_sum_5(0, [2, 5, 10, 4], 17))
print(group_sum_5(0, [2, 5, 10, 4], 12))
