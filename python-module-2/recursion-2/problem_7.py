def split_odd_10(nums):
    """
    Given an array of ints, is it possible to divide the ints into two groups, so that the sum of one group is a multiple of 10, and the sum of the other group is odd. Every int must be in one group or the other. Write a recursive helper method that takes whatever arguments you like, and make the initial call to your recursive helper from splitOdd10(). (No loops needed.)


    split_odd_10([5, 5, 5]) → True
    split_odd_10([5, 5, 6]) → False
    split_odd_10([5, 5, 6, 1]) → True
    """

    def helper(index, sum_10, sum_odd):
        if index == len(nums):
            return sum_10 % 10 == 0 and sum_odd % 2 == 1

        if helper(index + 1, sum_10 + nums[index], sum_odd):
            return True

        return helper(index + 1, sum_10, sum_odd + nums[index])

    return helper(0, 0, 0)


print(split_odd_10([5, 5, 5]))
print(split_odd_10([5, 5, 6]))
print(split_odd_10([5, 5, 6, 1]))
