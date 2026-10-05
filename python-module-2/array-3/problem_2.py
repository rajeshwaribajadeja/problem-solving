def fix_34(nums):
    """
    Return an array that contains exactly the same numbers as the given array, but rearranged so that every 3 is immediately followed by a 4. Do not move the 3's, but every other number may move. The array contains the same number of 3's and 4's, every 3 has a number after it that is not a 3, and a 3 appears in the array before any 4.

    fix_34([1, 3, 1, 4]) → [1, 3, 4, 1]
    fix_34([1, 3, 1, 4, 4, 3, 1]) → [1, 3, 4, 1, 1, 3, 4]
    fix_34([3, 2, 2, 4]) → [3, 4, 2, 2]
    """

    result = nums.copy()

    # Find each 3 and place a 4 immediately after it.
    four_index = 0

    for i in range(len(result)):
        if result[i] == 3:
            # Find the next 4 that has not been used.
            while result[four_index] != 4:
                four_index += 1

            # Swap the 4 into the position after 3.
            result[i + 1], result[four_index] = result[four_index], result[i + 1]

            four_index += 1

    return result


print(fix_34([1, 3, 1, 4]))
print(fix_34([1, 3, 1, 4, 4, 3, 1]))
print(fix_34([3, 2, 2, 4]))