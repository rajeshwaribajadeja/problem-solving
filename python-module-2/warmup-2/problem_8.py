def has271(nums):
    """
    Given an array of ints, return true if it contains a 2, 7, 1 pattern: a value, followed by the value plus 5, followed by the value minus 1. Additionally the 271 counts even if the "1" differs by 2 or less from the correct value.

    has271([1, 2, 7, 1]) → true
    has271([1, 2, 8, 1]) → false
    has271([2, 7, 1]) → true
    """

    for i in range(len(nums)-2):
        if (nums[i] == (nums[i+1] - 5)) and (nums[i] == (nums[i+2] + 1) or ((nums[i]-nums[i+2]) <= 2)):
            return True

    return False

print(has271([1, 2, 7, 1]))
print(has271([1, 2, 8, 1]))
print(has271([2, 7, 1]))
print(has271([10, 15, 9])) 