def split_53(nums):
    """
    Given an array of ints, is it possible to divide the ints into two groups, so that the sum of the two groups is the same, with these constraints: all the values that are multiple of 5 must be in one group, and all the values that are a multiple of 3 (and not a multiple of 5) must be in the other. (No loops needed.)


    split_53([1, 1]) → True
    split_53([1, 1, 1]) → False
    split_53([2, 4, 2]) → True
    """

    def helper(index, group_1, group_2):
        if index == len(nums):
            return group_1 == group_2

        if nums[index] % 5 == 0:
            return helper(index + 1, group_1 + nums[index], group_2)

        if nums[index] % 3 == 0:
            return helper(index + 1, group_1, group_2 + nums[index])

        if helper(index + 1, group_1 + nums[index], group_2):
            return True

        return helper(index + 1, group_1, group_2 + nums[index])

    return helper(0, 0, 0)


print(split_53([1, 1]))
print(split_53([1, 1, 1]))
print(split_53([2, 4, 2]))
