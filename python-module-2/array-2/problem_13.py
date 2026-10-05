def mod_three(nums):
    """
    Given an array of ints, return true if the array contains either
    3 even or 3 odd values all next to each other.

    mod_three([2, 1, 3, 5]) → True
    mod_three([2, 1, 2, 5]) → False
    mod_three([2, 4, 2, 5]) → True
    """

    for i in range(len(nums) - 2):
        if (nums[i] % 2 == nums[i + 1] % 2 and
            nums[i + 1] % 2 == nums[i + 2] % 2):
            return True

    return False


print(mod_three([2, 1, 3, 5]))
print(mod_three([2, 1, 2, 5]))
print(mod_three([2, 4, 2, 5]))
