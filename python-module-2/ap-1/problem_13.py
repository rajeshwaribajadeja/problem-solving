"""AP-1: score_up problem solution."""


def score_up(key: list, answers: list) -> int:
    """Return exam score: +4 for correct, -1 for incorrect, 0 for blank '?'.

    Args:
        key: The answer key list of correct answers.
        answers: The student's submitted answers ('?' for blank).

    Returns:
        The total computed exam score.

    Complexity:
        Time Complexity: O(N) where N is the length of key/answers.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> score_up(["a", "a", "b", "b"], ["a", "c", "b", "c"])
        6
        >>> score_up(["a", "a", "b", "b"], ["a", "a", "b", "c"])
        11
        >>> score_up(["a", "a", "b", "b"], ["a", "a", "b", "b"])
        16
    """
    score = 0
    for k, ans in zip(key, answers):
        if ans == "?":
            continue
        elif ans == k:
            score += 4
        else:
            score -= 1
    return score


if __name__ == "__main__":
    print(score_up(["a", "a", "b", "b"], ["a", "c", "b", "c"]))
    print(score_up(["a", "a", "b", "b"], ["a", "a", "b", "c"]))
    print(score_up(["a", "a", "b", "b"], ["a", "a", "b", "b"]))