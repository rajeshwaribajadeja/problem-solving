def either_24(nums):
    """
    Given an array of ints, return true if the array contains a 2 next
    to a 2 or a 4 next to a 4, but not both.

    either_24([1, 2, 2]) → True
    either_24([4, 4, 1]) → True
    either_24([4, 4, 1, 2, 2]) → False
    """

    has_22 = False
    has_44 = False

    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            has_22 = True
        if nums[i] == 4 and nums[i + 1] == 4:
            has_44 = True

    return has_22 != has_44


print(either_24([1, 2, 2]))
print(either_24([4, 4, 1]))
print(either_24([4, 4, 1, 2, 2]))
