def big_heights(heights, start, end):
    """
    (A variation on the sumHeights problem.) We have an array of heights, representing the altitude along a walking trail. Given start/end indexes into the array, return the number of "big" steps for a walk starting at the start index and ending at the end index. We'll say that step is big if it is 5 or more up or down. The start end end index will both be valid indexes into the array with start <= end.

    big_heights([5, 3, 6, 7, 2], 2, 4) → 1
    big_heights([5, 3, 6, 7, 2], 0, 1) → 0
    big_heights([5, 3, 6, 7, 2], 0, 4) → 1
    """

    count = 0

    for i in range(start, end):
        change = abs(heights[i + 1] - heights[i])

        if change >= 5:
            count += 1

    return count


print(big_heights([5, 3, 6, 7, 2], 2, 4))
print(big_heights([5, 3, 6, 7, 2], 0, 1))
print(big_heights([5, 3, 6, 7, 2], 0, 4))