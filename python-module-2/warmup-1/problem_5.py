def start_hi(str):
    """
    Given a string, return true if the string starts with "hi" and false otherwise.


    start_hi("hi there") → true
    start_hi("hi") → true
    start_hi("hello hi") → false

    """

    # return str.startswith("hi")
    return str[:2] == "hi"

print(start_hi("hi there"))
print(start_hi("hi"))
print(start_hi("hello hi"))