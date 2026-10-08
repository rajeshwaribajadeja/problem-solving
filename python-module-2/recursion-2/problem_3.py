def group_no_adj(start, nums, target):
    """
    Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given target with this additional constraint: If a value in the array is chosen to be in the group, the value immediately following it in the array must not be chosen. (No loops needed.)


    group_no_adj(0, [2, 5, 10, 4], 12) → True
    group_no_adj(0, [2, 5, 10, 4], 14) → False
    group_no_adj(0, [2, 5, 10, 4], 7) → False
    """

    if target == 0:
        return True

    if start >= len(nums):
        return False

    if group_no_adj(start + 2, nums, target - nums[start]):
        return True

    return group_no_adj(start + 1, nums, target)


print(group_no_adj(0, [2, 5, 10, 4], 12))
print(group_no_adj(0, [2, 5, 10, 4], 14))
print(group_no_adj(0, [2, 5, 10, 4], 7))
