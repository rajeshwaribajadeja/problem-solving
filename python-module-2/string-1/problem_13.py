def last_two(str):
    """
    Given a string of any length, return a new string where the last 2 chars, if present, are swapped, so "coding" yields "codign".

    last_two("coding") → "codign"
    last_two("cat") → "cta"
    last_two("ab") → "ba"
    """
    if len(str) < 2:
        return str

    return str[:-2] + str[-1] + str[-2]

print(last_two("coding"))
print(last_two("cat"))
print(last_two("ab"))