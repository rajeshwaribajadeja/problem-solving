def scores_increasing(scores):
    """
    Given an array of scores, return true if each score is equal or greater than the one before. The array will be length 2 or more.


    scores_increasing([1, 3, 4]) → True
    scores_increasing([1, 3, 2]) → False
    scores_increasing([1, 1, 4]) → True
    """

    for i in range(1, len(scores)):
        if scores[i] < scores[i - 1]:
            return False

    return True


print(scores_increasing([1, 3, 4]))
print(scores_increasing([1, 3, 2]))
print(scores_increasing([1, 1, 4]))