def ntwice(str, n):
    """
    Given a string and an int n, return a string made of the first and last n chars from the string. The string length will be at least n.


    ntwice("Hello", 2) → "Helo"
    ntwice("Chocolate", 3) → "Choate"
    ntwice("Chocolate", 1) → "Ce"
    """
    return str[:n] + str[-n:]

print(ntwice("Hello", 2))
print(ntwice("Chocolate", 3))
print(ntwice("Chocolate", 1))