def sum_heights(heights, start, end):
    """
    We have an array of heights, representing the altitude along a walking trail. Given start/end indexes into the array, return the sum of the changes for a walk beginning at the start index and ending at the end index. For example, with the heights {5, 3, 6, 7, 2} and start=2, end=4 yields a sum of 1 + 5 = 6. The start end end index will both be valid indexes into the array with start <= end.

    sum_heights([5, 3, 6, 7, 2], 2, 4) → 6
    sum_heights([5, 3, 6, 7, 2], 0, 1) → 2
    sum_heights([5, 3, 6, 7, 2], 0, 4) → 11
    """

    total = 0

    for i in range(start, end):
        total += abs(heights[i + 1] - heights[i])

    return total


print(sum_heights([5, 3, 6, 7, 2], 2, 4))
print(sum_heights([5, 3, 6, 7, 2], 0, 1))
print(sum_heights([5, 3, 6, 7, 2], 0, 4))