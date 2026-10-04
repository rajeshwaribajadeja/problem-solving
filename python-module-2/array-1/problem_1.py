def no23(nums):
    """
    Given an int array length 2, return true if it does not contain a 2 or 3.

    no23([4, 5]) → True
    no23([4, 2]) → False
    no23([3, 5]) → False
    """
    return (2 not in nums) and (3 not in nums)


print(no23([4, 5]))
print(no23([4, 2]))
print(no23([3, 2]))
