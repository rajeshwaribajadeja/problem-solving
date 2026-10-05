def count_clumps(nums):
    """
    Say that a "clump" in an array is a series of 2 or more adjacent elements of the same value. Return the number of clumps in the given array.

    count_clumps([1, 2, 2, 3, 4, 4]) → 2
    count_clumps([1, 1, 2, 1, 1]) → 2
    count_clumps([1, 1, 1, 1, 1]) → 1
    """ 

    count = 0
    i = 0

    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            count += 1

            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

        i += 1

    return count


print(count_clumps([1, 2, 2, 3, 4, 4]))
print(count_clumps([1, 1, 2, 1, 1]))
print(count_clumps([1, 1, 1, 1, 1]))
