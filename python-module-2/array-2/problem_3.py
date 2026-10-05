def more14(nums):
    """
    Given an array of ints, return true if the number of 1's
    is greater than the number of 4's.

    more14([1, 4, 1]) → True
    more14([1, 4, 1, 4]) → False
    more14([1, 1]) → True
    """

    # count_1 = 0
    # count_4 = 0

    # for num in nums:
    #     if num == 1:
    #         count_1 += 1
    #     elif num == 4:
    #         count_4 += 1

    # return count_1 > count_4

    return nums.count(1) > nums.count(4)


print(more14([1, 4, 1]))
print(more14([1, 4, 1, 4]))
print(more14([1, 1]))
