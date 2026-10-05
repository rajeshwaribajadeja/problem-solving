def no_neg(nums):
    """
    Given a list of integers, return a list of the integers,
    omitting any that are less than 0.


    no_neg([1, -2]) → [1]
    no_neg([-3, -3, 3, 3]) → [3, 3]
    no_neg([-1, -1, -1]) → []
    """

    return list(filter(lambda x: x >= 0, nums))


print(no_neg([1, -2]))
print(no_neg([-3, -3, 3, 3]))
print(no_neg([-1, -1, -1]))
