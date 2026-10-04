def tea_party(tea, candy):
    """
    We are having a party with amounts of tea and candy.
    Return the int outcome of the party:
    0 = bad, 1 = good, 2 = great.

    A party is good (1) if both tea and candy are at least 5.
    If either tea or candy is at least double the amount of the other,
    the party is great (2).
    If either tea or candy is less than 5, the party is always bad (0).

    tea_party(6, 8) → 1
    tea_party(3, 8) → 0
    tea_party(20, 6) → 2
    """

    return 0 if tea < 5 or candy < 5 else 2 if tea >= candy * 2 or candy >= tea * 2 else 1

print(tea_party(6, 8))
print(tea_party(3, 8))
print(tea_party(20, 6))


    