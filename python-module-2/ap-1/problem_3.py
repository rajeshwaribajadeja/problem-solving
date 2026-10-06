def scores_clump(scores):
    """
    Given an array of scores sorted in increasing order, return True
    if the array contains 3 adjacent scores that differ from each
    other by at most 2.


    scores_clump([3, 4, 5]) → True
    scores_clump([3, 4, 6]) → False
    scores_clump([1, 3, 5, 5]) → True
    """

    for i in range(len(scores) - 2):
        # if scores[i + 2] - scores[i] <= 2:
        #     return True
        if (scores[i + 1] - scores[i] <= 2 and scores[i + 2] - scores[i + 1] <= 2 and scores[i + 2] - scores[i] <= 2):
            return True

    return False


print(scores_clump([3, 4, 5]))
print(scores_clump([3, 4, 6]))
print(scores_clump([1, 3, 5, 5]))