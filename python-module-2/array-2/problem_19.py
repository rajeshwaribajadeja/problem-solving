def shift_left(nums):
    """
    Return an array that is "left shifted" by one -- so {6, 2, 5, 3} returns {2, 5, 3, 6}. You may modify and return the given array, or return a new array.


    shift_left([6, 2, 5, 3]) → [2, 5, 3, 6]
    shift_left([1, 2]) → [2, 1]
    shift_left([1]) → [1]
    """

    if len(nums) <= 1:
        return nums

    return nums[1:] + nums[:1]


print(shift_left([6, 2, 5, 3]))
print(shift_left([1, 2]))
print(shift_left([1]))
