def score_up(key, answers):
    """
    The "key" array is an array containing the correct answers to an exam, like {"a", "a", "b", "b"}. the "answers" array contains a student's answers, with "?" representing a question left blank. The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer.


    score_up(["a", "a", "b", "b"], ["a", "c", "b", "c"]) → 6
    score_up(["a", "a", "b", "b"], ["a", "a", "b", "c"]) → 11
    score_up(["a", "a", "b", "b"], ["a", "a", "b", "b"]) → 16
    """

    score = 0

    for i in range(len(key)):
        if answers[i] == "?":
            score += 0
        elif answers[i] == key[i]:
            score += 4
        else:
            score -= 1

    return score


print(score_up(["a", "a", "b", "b"], ["a", "c", "b", "c"]))
print(score_up(["a", "a", "b", "b"], ["a", "a", "b", "c"]))
print(score_up(["a", "a", "b", "b"], ["a", "a", "b", "b"]))