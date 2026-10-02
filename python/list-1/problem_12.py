def has23(nums):
    """
    Given an array of ints length 2, return True if 2 or 3 is in the array.

    has23([2, 5]) → True
    has23([4, 3]) → True
    has23([4, 5]) → False
    """
    return 2 in nums or 3 in nums

print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))
