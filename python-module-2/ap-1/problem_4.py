def scores_average(scores):
    """
    Given an array of scores, compute the int average of the first half and the second half, and return whichever is larger. We'll say that the second half begins at index length/2. The array length will be at least 2. To practice decomposition, write a separate helper method
    int average(int[] scores, int start, int end) { which computes the average of the elements between indexes start..end. Call your helper method twice to implement scoresAverage(). Write your helper method after your scoresAverage() method in the JavaBat text area. Normally you would compute averages with doubles, but here we use ints so the expected results are exact.


    scores_average([2, 2, 4, 4]) → 4
    scores_average([4, 4, 4, 2, 2, 2]) → 4
    scores_average([3, 4, 5, 1, 2, 3]) → 4
    """

    mid = len(scores) // 2

    first_average = average(scores, 0, mid)
    second_average = average(scores, mid, len(scores))

    return max(first_average, second_average)


def average(scores, start, end):
    total = 0

    for i in range(start, end):
        total += scores[i]

    return total // (end - start)


print(scores_average([2, 2, 4, 4]))
print(scores_average([4, 4, 4, 2, 2, 2]))
print(scores_average([3, 4, 5, 1, 2, 3]))