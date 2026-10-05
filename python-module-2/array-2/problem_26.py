def zero_max(nums):
    """
    Return a version of the given array where each zero value in the array is replaced by the largest odd value to the right of the zero in the array. If there is no odd value to the right of the zero, leave the zero as a zero.

    zero_max([0, 5, 0, 3]) → [5, 5, 3, 3]
    zero_max([0, 4, 0, 3]) → [3, 4, 3, 3]
    zero_max([0, 1, 0]) → [1, 1, 0]
    """

    result = nums.copy()

    for i in range(len(nums)):
        if nums[i] == 0:
            largest_odd = 0

            for j in range(i + 1, len(nums)):
                if nums[j] % 2 == 1:
                    largest_odd = max(largest_odd, nums[j])

            if largest_odd != 0:
                result[i] = largest_odd

    return result


print(zero_max([0, 5, 0, 3]))
print(zero_max([0, 4, 0, 3]))
print(zero_max([0, 1, 0]))
