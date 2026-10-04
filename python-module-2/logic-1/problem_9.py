def fizz_string(str):
    """
    Given a string str, if the string starts with "f" return "Fizz".
    If the string ends with "b" return "Buzz".
    If both the "f" and "b" conditions are true, return "FizzBuzz".
    In all other cases, return the string unchanged.

    fizz_string("fig") → "Fizz"
    fizz_string("dib") → "Buzz"
    fizz_string("fib") → "FizzBuzz"
    """

    starts_f = str[0] == "f"
    ends_b = str[-1] == "b"

    return "FizzBuzz" if starts_f and ends_b else "Fizz" if starts_f else "Buzz" if ends_b else str


print(fizz_string("fig"))
print(fizz_string("dib"))
print(fizz_string("fib"))