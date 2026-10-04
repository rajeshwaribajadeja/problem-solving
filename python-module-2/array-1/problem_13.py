def unlucky1(nums):
    """
    We'll say that a 1 immediately followed by a 3 in an array is
    an "unlucky" 1. Return true if the given array contains an unlucky
    1 in the first 2 or last 2 positions in the array.

    unlucky1([1, 3, 4, 5]) → True
    unlucky1([2, 1, 3, 4, 5]) → True
    unlucky1([1, 1, 1]) → False
    """

    if len(nums) >= 2:
        if nums[0] == 1 and nums[1] == 3:
            return True

        if nums[-2] == 1 and nums[-1] == 3:
            return True

    return False


print(unlucky1([1, 3, 4, 5]))
print(unlucky1([2, 1, 3, 4, 5]))
print(unlucky1([1, 1, 1]))
