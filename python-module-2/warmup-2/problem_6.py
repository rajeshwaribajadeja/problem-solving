def array667(nums):
    """
    Given an array of ints, return the number of times that two 6's are next to each other in the array. Also count instances where the second "6" is actually a 7.

    array667([6, 6, 2]) → 1
    array667([6, 6, 2, 6]) → 1
    array667([6, 7, 2, 6]) → 1
    """

    count = 0
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1] == 6 or (nums[i] == 6 and nums[i+1] == 7):
            count += 1

    return count

print(array667([6, 6, 2]))
print(array667([6, 6, 2, 6]))
print(array667([6, 7, 2, 6]))