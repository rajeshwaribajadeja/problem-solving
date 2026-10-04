def sum_digits(str):
    """
    Given a string, return the sum of the digits 0-9 that appear in the string, ignoring all other characters. Return 0 if there are no digits in the string. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)


    sum_digits("aa1bc2d3") → 6
    sum_digits("aa11b33") → 8
    sum_digits("Chocolate") → 0
    """
    total = 0

    for ch in str:
        if ch.isdigit():
            total += int(ch)

    return total

print(sum_digits("aa1bc2d3"))
print(sum_digits("aa11b33"))
print(sum_digits("Chocolate"))