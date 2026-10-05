def two_two(nums):
    """
    Given an array of ints, return true if every 2 that appears
    in the array is next to another 2.

    two_two([4, 2, 2, 3]) → True
    two_two([2, 2, 4]) → True
    two_two([2, 2, 4, 2]) → False
    """

    i = 0
    while i < len(nums):
        if nums[i] == 2:
            if i + 1 >= len(nums) or nums[i + 1] != 2:
                return False
            i += 2
        else:
            i += 1
    return True


print(two_two([4, 2, 2, 3]))
print(two_two([2, 2, 4]))
print(two_two([2, 2, 4, 2]))
