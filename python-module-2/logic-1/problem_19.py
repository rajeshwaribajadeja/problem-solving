def green_ticket(a, b, c):
    """
    You have a green lottery ticket, with ints a, b, and c on it.

    If the numbers are all different, return 0.
    If all of the numbers are the same, return 20.
    If two of the numbers are the same, return 10.

    green_ticket(1, 2, 3) → 0
    green_ticket(2, 2, 2) → 20
    green_ticket(1, 1, 2) → 10
    """

    if a == b == c:
        return 20

    if a == b or a == c or b == c:
        return 10

    return 0


print(green_ticket(1, 2, 3))
print(green_ticket(2, 2, 2))
print(green_ticket(1, 1, 2))