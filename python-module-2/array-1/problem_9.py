def swap_ends(nums):
    """
    Given an array of ints, swap the first and last elements in the array.
    Return the modified array. The array length will be at least 1.

    swap_ends([1, 2, 3, 4]) → [4, 2, 3, 1]
    swap_ends([1, 2, 3]) → [3, 2, 1]
    swap_ends([8, 6, 7, 9, 5]) → [5, 6, 7, 9, 8]
    """

    nums[0], nums[-1] = nums[-1], nums[0]

    return nums


print(swap_ends([1, 2, 3, 4]))
print(swap_ends([1, 2, 3]))
print(swap_ends([8, 6, 7, 9, 5]))
