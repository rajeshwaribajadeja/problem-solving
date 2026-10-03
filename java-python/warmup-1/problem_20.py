def everynth(str, n):
    """
    Given a non-empty string and an int N, return the string made starting with char 0, and then every Nth char of the string. So if N is 3, use char 0, 3, 6, ... and so on. N is 1 or more.


    everynth("Miracle", 2) → "Mrce"
    everynth("abcdefg", 2) → "aceg"
    everynth("abcdefg", 3) → "adg"
    """

    return str[::n]

print(everynth("Miracle", 2))
print(everynth("abcdefg", 2))
print(everynth("abcdefg", 3))
