def parrot_trouble(talking, hour):
    """
    We have a loud parrot. The "hour" parameter is the current hour in the range 0..23. We are in trouble if the parrot is talking and the hour is between 7 and 20. Return True if we are in trouble.


    parrot_trouble(True, 6) → False
    parrot_trouble(True, 7) → True
    parrot_trouble(False, 6) → False
    """
    return talking and (hour < 7 or hour > 20)


print(parrot_trouble(True, 6))
print(parrot_trouble(True, 7))
print(parrot_trouble(False, 6))