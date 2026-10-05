def blackjack(a, b):
    """
    Given 2 int values greater than 0, return whichever value is
    nearest to 21 without going over. Return 0 if they both go over.

    blackjack(19, 21) → 21
    blackjack(21, 19) → 21
    blackjack(19, 22) → 19
    """

    if a > 21 and b > 21:
        return 0
    elif a > 21:
        return b
    elif b > 21:
        return a
    else:
        return max(a, b)


print(blackjack(19, 21))
print(blackjack(21, 19))
print(blackjack(19, 22))