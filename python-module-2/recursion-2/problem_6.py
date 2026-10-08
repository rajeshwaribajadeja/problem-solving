def split_array(nums):
    """
    Given an array of ints, is it possible to divide the ints into two groups, so that the sums of the two groups are the same. Every int must be in one group or the other. Write a recursive helper method that takes whatever arguments you like, and make the initial call to your recursive helper from splitArray(). (No loops needed.)


    split_array([2, 2]) → True
    split_array([2, 3]) → False
    split_array([5, 2, 3]) → True
    """

    def helper(index, group_1, group_2):
        if index == len(nums):
            return group_1 == group_2

        if helper(index + 1, group_1 + nums[index], group_2):
            return True

        return helper(index + 1, group_1, group_2 + nums[index])

    return helper(0, 0, 0)


print(split_array([2, 2]))
print(split_array([2, 3]))
print(split_array([5, 2, 3]))
