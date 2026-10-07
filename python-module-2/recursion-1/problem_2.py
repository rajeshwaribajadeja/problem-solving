def bunny_ears(n):
    """
    We have a number of bunnies and each bunny has two big floppy ears.
    Compute the total number of ears recursively (without loops or multiplication).


    bunny_ears(0) → 0
    bunny_ears(1) → 2
    bunny_ears(2) → 4
    """

    # if n == 0:
    #     return 0

    return 0 if n == 0 else 2 + bunny_ears(n - 1)


print(bunny_ears(0))
print(bunny_ears(1))
print(bunny_ears(2))
