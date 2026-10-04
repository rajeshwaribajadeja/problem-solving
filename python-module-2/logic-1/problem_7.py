def answer_cell(is_morning, is_mom, is_asleep):
    """
    Your cell phone rings. Return true if you should answer it.
    Normally you answer, except in the morning you only answer if
    it is your mom calling. In all cases, if you are asleep, you
    do not answer.

    answer_cell(False, False, False) → True
    answer_cell(False, False, True) → False
    answer_cell(True, False, False) → False
    """

    return not is_asleep and (not is_morning or is_mom)


print(answer_cell(False, False, False))
print(answer_cell(False, False, True))
print(answer_cell(True, False, False))