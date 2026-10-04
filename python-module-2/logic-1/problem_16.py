def without_doubles(die1, die2, no_doubles):
    """
    Return the sum of two 6-sided dice rolls.
    If no_doubles is true and both dice show the same value,
    increment one die to the next value, wrapping around to 1
    if its value was 6.

    without_doubles(2, 3, True) → 5
    without_doubles(3, 3, True) → 7
    without_doubles(3, 3, False) → 6
    """

    if no_doubles and die1 == die2:
        if die2 == 6:
            die2 = 1
        else:
            die2 += 1

    return die1 + die2


print(without_doubles(2, 3, True))
print(without_doubles(3, 3, True))
print(without_doubles(3, 3, False))