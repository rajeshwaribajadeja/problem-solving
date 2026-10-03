def sum3(nums):
    """
    Given an array of ints length 3, return the sum of all the elements.

    sum3([1, 2, 3]) → 6
    sum3([5, 11, 2]) → 18
    sum3([7, 0, 0]) → 7
    """

    # return sum(nums) # sum() is a built in function that returns the sum of all the elements in an iterable

    # return nums[0] + nums[1] + nums[2]

    sum = 0
    for num in nums:
        sum+=num
    return sum


print(sum3([1, 2, 3]))
print(sum3([5, 11, 2]))
print(sum3([7, 0, 0]))
