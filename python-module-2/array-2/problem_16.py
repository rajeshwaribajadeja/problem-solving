def same_ends(nums, n):
    """
    Return true if the group of N numbers at the start and end
    of the array are the same.

    same_ends([5, 6, 45, 99, 13, 5, 6], 1) → False
    same_ends([5, 6, 45, 99, 13, 5, 6], 2) → True
    same_ends([5, 6, 45, 99, 13, 5, 6], 3) → False
    """

    return nums[:n] == nums[-n:] if n > 0 else True


print(same_ends([5, 6, 45, 99, 13, 5, 6], 1))
print(same_ends([5, 6, 45, 99, 13, 5, 6], 2))
print(same_ends([5, 6, 45, 99, 13, 5, 6], 3))
