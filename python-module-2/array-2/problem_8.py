def is_everywhere(nums, val):
    """
    We'll say that a value is "everywhere" in an array if for every pair
    of adjacent elements in the array, at least one of the pair is that value.

    is_everywhere([1, 2, 1, 3], 1) → True
    is_everywhere([1, 2, 1, 3], 2) → False
    is_everywhere([1, 2, 1, 3, 4], 1) → False
    """

    for i in range(len(nums) - 1):
        if nums[i] == val or nums[i + 1] == val:
            continue
        else:
            return False

    return True


print(is_everywhere([1, 2, 1, 3], 1))
print(is_everywhere([1, 2, 1, 3], 2))
print(is_everywhere([1, 2, 1, 3, 4], 1))
