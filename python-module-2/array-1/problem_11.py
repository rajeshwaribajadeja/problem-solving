def max_triple(nums):
    """
    Given an array of ints of odd length, look at the first, last,
    and middle values in the array and return the largest.

    max_triple([1, 2, 3]) → 3
    max_triple([1, 5, 3]) → 5
    max_triple([5, 2, 3]) → 5
    """

    middle = len(nums) // 2

    return max(nums[0], nums[middle], nums[-1])

    # middle = len(nums) // 2

    # largest = nums[0]

    # if nums[middle] > largest:
    #     largest = nums[middle]

    # if nums[-1] > largest:
    #     largest = nums[-1]

    # return largest


print(max_triple([1, 2, 3]))
print(max_triple([1, 5, 3]))
print(max_triple([5, 2, 3]))
