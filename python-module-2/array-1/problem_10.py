def mid_three(nums):
    """
    Given an array of ints of odd length, return a new array length 3
    containing the elements from the middle of the array.

    mid_three([1, 2, 3, 4, 5]) → [2, 3, 4]
    mid_three([8, 6, 7, 5, 3, 0, 9]) → [7, 5, 3]
    mid_three([1, 2, 3]) → [1, 2, 3]
    """

    middle = len(nums) // 2

    return nums[middle - 1:middle + 2]


print(mid_three([1, 2, 3, 4, 5]))
print(mid_three([8, 6, 7, 5, 3, 0, 9]))
print(mid_three([1, 2, 3]))