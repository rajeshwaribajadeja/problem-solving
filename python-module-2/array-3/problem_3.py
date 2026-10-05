def fix_45(nums):
    """
    Return an array that contains exactly the same numbers as the given array, but rearranged so that every 4 is immediately followed by a 5. Do not move the 4's, but every other number may move. The array contains the same number of 4's and 5's, and every 4 has a number after it that is not a 4. In this version, 5's may appear anywhere in the original array.

    fix_45([5, 4, 9, 4, 9, 5]) → [9, 4, 5, 4, 5, 9]
    fix_45([1, 4, 1, 5]) → [1, 4, 5, 1]
    fix_45([1, 4, 1, 5, 5, 4, 1]) → [1, 4, 5, 1, 1, 4, 5]
    """

    result = nums.copy()

    # Find the 4's and place a 5 immediately after each one.
    five_index = 0

    for i in range(len(result)):
        if result[i] == 4:
            # Find the next unused 5.
            while result[five_index] != 5:
                five_index += 1

            # Swap the 5 into the position after the 4.
            result[i + 1], result[five_index] = result[five_index], result[i + 1]

            five_index += 1

    return result


print(fix_45([5, 4, 9, 4, 9, 5]))
print(fix_45([1, 4, 1, 5]))
print(fix_45([1, 4, 1, 5, 5, 4, 1]))
