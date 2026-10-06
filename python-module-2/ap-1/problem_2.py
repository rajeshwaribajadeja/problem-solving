def scores_100(scores):
    """
    Given an array of scores, return true if there are scores of 100 next to each other in the array. The array length will be at least 2.


    scores_100([1, 100, 100]) → True
    scores_100([1, 100, 99, 100]) → False
    scores_100([100, 1, 100, 100]) → True
    """

    for i in range(len(scores) - 1):
        if scores[i] == 100 and scores[i + 1] == 100:
            return True

    return False


print(scores_100([1, 100, 100]))
print(scores_100([1, 100, 99, 100]))
print(scores_100([100, 1, 100, 100]))