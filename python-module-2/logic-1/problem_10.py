def fizz_string2(n):
    """
    Given an int n, return the string form of the number followed by "!". So the int 6 yields "6!". Except if the number is divisible by 3 use "Fizz" instead of the number, and if the number is divisible by 5 use "Buzz", and if divisible by both 3 and 5, use "FizzBuzz". Note: the % "mod" operator computes the remainder after division, so 23 % 10 yields 3. What will the remainder be when one number divides evenly into another? 

    fizz_string2(1) → "1!"
    fizz_string2(2) → "2!"
    fizz_string2(3) → "Fizz!"
    """

    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz!"
    elif n % 3 == 0:
        return "Fizz!"
    elif n % 5 == 0:
        return "Buzz!"
    else:
        return str(n) + "!"


print(fizz_string2(1))
print(fizz_string2(2))
print(fizz_string2(3))