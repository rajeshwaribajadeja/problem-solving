def array_6(nums, index):
    """
    Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.


    array_6([1, 6, 4], 0) → True
    array_6([1, 4], 0) → False
    array_6([6], 0) → True
    """

    if index == len(nums):
        return False

    # if nums[index] == 6:
    #     return True

    return True if nums[index] == 6 else array_6(nums, index + 1)


print(array_6([1, 6, 4], 0))
print(array_6([1, 4], 0))
print(array_6([6], 0))
