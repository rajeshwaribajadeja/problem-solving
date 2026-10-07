def sum_heights_2(heights, start, end):
    """
    (A variation on the sumHeights problem.) We have an array of heights, representing the altitude along a walking trail. Given start/end indexes into the array, return the sum of the changes for a walk beginning at the start index and ending at the end index, however increases in height count double. For example, with the heights {5, 3, 6, 7, 2} and start=2, end=4 yields a sum of 1*2 + 5 = 7. The start end end index will both be valid indexes into the array with start <= end.


    sum_heights_2([5, 3, 6, 7, 2], 2, 4) → 7
    sum_heights_2([5, 3, 6, 7, 2], 0, 1) → 2
    sum_heights_2([5, 3, 6, 7, 2], 0, 4) → 15
    """

    total = 0

    for i in range(start, end):
        if heights[i + 1] > heights[i]:
            total += (heights[i + 1] - heights[i]) * 2
        else:
            total += heights[i] - heights[i + 1]

    return total


print(sum_heights_2([5, 3, 6, 7, 2], 2, 4))
print(sum_heights_2([5, 3, 6, 7, 2], 0, 1))
print(sum_heights_2([5, 3, 6, 7, 2], 0, 4))