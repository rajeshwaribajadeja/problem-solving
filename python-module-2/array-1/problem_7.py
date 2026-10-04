def make_middle(nums):
    """
    Given an array of ints of even length, return a new array length 2
    containing the middle two elements from the original array.

    make_middle([1, 2, 3, 4]) → [2, 3]
    make_middle([7, 1, 2, 3, 4, 9]) → [2, 3]
    make_middle([1, 2]) → [1, 2]
    """

    middle = len(nums) // 2

    return [nums[middle - 1], nums[middle]]


print(make_middle([1, 2, 3, 4]))
print(make_middle([7, 1, 2, 3, 4, 9]))
print(make_middle([1, 2]))
