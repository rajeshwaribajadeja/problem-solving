def not_alone(nums, val):
    """
    We'll say that an element in an array is "alone" if there are values before and after it, and those values are different from it. Return a version of the given array where every instance of the given value which is alone is replaced by whichever value to its left or right is larger.

    not_alone([1, 2, 3], 2) → [1, 3, 3]
    not_alone([1, 2, 3, 2, 5, 2], 2) → [1, 3, 3, 5, 5, 2]
    not_alone([3, 4], 3) → [3, 4]
    """

    result = nums.copy()

    for i in range(1, len(nums) - 1):
        if nums[i] == val:
            if nums[i - 1] != val and nums[i + 1] != val:
                result[i] = max(nums[i - 1], nums[i + 1])

    return result


print(not_alone([1, 2, 3], 2))
print(not_alone([1, 2, 3, 2, 5, 2], 2))
print(not_alone([3, 4], 3))
