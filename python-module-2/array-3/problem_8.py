def max_mirror(nums):
    """
    We'll say that a "mirror" section in an array is a group of contiguous elements such that somewhere in the array, the same group appears in reverse order. For example, the largest mirror section in {1, 2, 3, 8, 9, 3, 2, 1} is length 3 (the {1, 2, 3} part). Return the size of the largest mirror section found in the given array.


    max_mirror([1, 2, 3, 8, 9, 3, 2, 1]) → 3
    max_mirror([1, 2, 1, 4]) → 3
    max_mirror([7, 1, 2, 9, 7, 2, 1]) → 2
    """

    max_length = 0

    for i in range(len(nums)):
        for j in range(len(nums)):
            length = 0

            while (i + length < len(nums) and
                   j - length >= 0 and
                   nums[i + length] == nums[j - length]):
                length += 1

            max_length = max(max_length, length)

    return max_length


print(max_mirror([1, 2, 3, 8, 9, 3, 2, 1]))
print(max_mirror([1, 2, 1, 4]))
print(max_mirror([7, 1, 2, 9, 7, 2, 1]))
