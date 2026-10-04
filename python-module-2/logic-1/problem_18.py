def red_ticket(a, b, c):
    """
    You have a red lottery ticket showing ints a, b, and c, each of
    which is 0, 1, or 2.

    If they are all 2, the result is 10.
    Otherwise if they are all the same, the result is 5.
    Otherwise, if both b and c are different from a, the result is 1.
    Otherwise the result is 0.

    red_ticket(2, 2, 2) → 10
    red_ticket(2, 2, 1) → 0
    red_ticket(0, 0, 0) → 5
    """

    if a == b == c == 2:
        return 10

    if a == b == c:
        return 5

    if a != b and a != c:
        return 1

    return 0


print(red_ticket(2, 2, 2))
print(red_ticket(2, 2, 1))
print(red_ticket(0, 0, 0))