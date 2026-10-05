def fizz_buzz(start, end):
    """
    Consider the series of numbers beginning at start and running up to
    but not including end. Return a new array containing the string form
    of these numbers, except multiples of 3 are "Fizz", multiples of 5
    are "Buzz", and multiples of both 3 and 5 are "FizzBuzz".

    fizz_buzz(1, 6) → ["1", "2", "Fizz", "4", "Buzz"]
    fizz_buzz(1, 8) → ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"]
    fizz_buzz(1, 11) → ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]
    """

    result = []

    for num in range(start, end):
        if num % 3 == 0 and num % 5 == 0:
            result.append("FizzBuzz")
        elif num % 3 == 0:
            result.append("Fizz")
        elif num % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(num))

    return result


print(fizz_buzz(1, 6))
print(fizz_buzz(1, 8))
print(fizz_buzz(1, 11))
