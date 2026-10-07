def array_220(nums, index):
    """
    Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that value times 10. We'll use the convention of considering only the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.


    array_220([1, 2, 20], 0) → True
    array_220([3, 30], 0) → True
    array_220([3], 0) → False
    """

    if index >= len(nums) - 1:
        return False

    if nums[index + 1] == nums[index] * 10:
        return True

    return array_220(nums, index + 1)


print(array_220([1, 2, 20], 0))
print(array_220([3, 30], 0))
print(array_220([3], 0))
