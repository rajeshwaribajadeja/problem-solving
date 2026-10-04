def sum_numbers(str):
    """
    Given a string, return the sum of the numbers appearing in the string,
    ignoring all other characters. A number is a series of 1 or more digit
    chars in a row.

    sum_numbers("abc123xyz") → 123
    sum_numbers("aa11b33") → 44
    sum_numbers("7 11") → 18
    """

    total = 0
    number = ""

    for ch in str:
        if ch.isdigit():
            number += ch
        else:
            if number != "":
                total += int(number)
                number = ""

    if number != "":
        total += int(number)

    return total


print(sum_numbers("abc123xyz"))
print(sum_numbers("aa11b33"))
print(sum_numbers("7 11"))
