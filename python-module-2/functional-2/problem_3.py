def no_teen(nums):
    """
    Given a list of integers, return a list of those numbers,
    omitting any that are between 13 and 19 inclusive.


    no_teen([12, 13, 19, 20]) → [12, 20]
    no_teen([1, 14, 1]) → [1, 1]
    no_teen([15]) → []
    """

    return list(filter(lambda x: x < 13 or x > 19, nums))


print(no_teen([12, 13, 19, 20]))
print(no_teen([1, 14, 1]))
print(no_teen([15]))
