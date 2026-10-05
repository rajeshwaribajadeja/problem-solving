def triple_up(nums):
    """
    Return true if the array contains three increasing adjacent numbers.

    triple_up([1, 4, 5, 6, 2]) → True
    triple_up([1, 2, 3]) → True
    triple_up([1, 2, 4]) → False
    """

    for i in range(len(nums) - 2):
        if nums[i + 1] == nums[i] + 1 and nums[i + 2] == nums[i] + 2:
            return True

    return False


print(triple_up([1, 4, 5, 6, 2]))
print(triple_up([1, 2, 3]))
print(triple_up([1, 2, 4]))
