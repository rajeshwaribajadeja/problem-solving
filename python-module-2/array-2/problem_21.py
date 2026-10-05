def pre_4(nums):
    """
    Given a non-empty array of ints, return a new array containing the elements from the original array that come before the first 4 in the original array. The original array will contain at least one 4.

    pre_4([1, 2, 4, 1]) → [1, 2]
    pre_4([3, 1, 4]) → [3, 1]
    pre_4([1, 4, 4]) → [1]
    """

    result = []

    for num in nums:
        if num == 4:
            break

        result.append(num)

    return result


print(pre_4([1, 2, 4, 1]))
print(pre_4([3, 1, 4]))
print(pre_4([1, 4, 4]))
