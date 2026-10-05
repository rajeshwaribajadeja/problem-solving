def match_up(nums1, nums2):
    """
    Given arrays nums1 and nums2 of the same length, for every element in nums1, consider the corresponding element in nums2 (at the same index). Return the count of the number of times that the two elements differ by 2 or less, but are not equal.



    match_up([1, 2, 3], [2, 3, 10]) → 2
    match_up([1, 2, 3], [2, 3, 5]) → 3
    match_up([1, 2, 3], [2, 3, 3]) → 2
    """

    count = 0

    for i in range(len(nums1)):
        difference = abs(nums1[i] - nums2[i])

        if difference <= 2 and difference != 0:
            count += 1

    return count


print(match_up([1, 2, 3], [2, 3, 10]))
print(match_up([1, 2, 3], [2, 3, 5]))
print(match_up([1, 2, 3], [2, 3, 3]))
