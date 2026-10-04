def repeat_separator(word, sep, count):
    """
    Given two strings, word and a separator sep, return a big string made of count occurrences of the word, separated by the separator string.


    repeat_separator("Word", "X", 3) → "WordXWordXWord"
    repeat_separator("This", "And", 2) → "ThisAndThis"
    repeat_separator("This", "And", 1) → "This"
    """
    return word + (sep + word) * (count-1)

print(repeat_separator("Word", "X", 3))
print(repeat_separator("This", "And", 2))
print(repeat_separator("This", "And", 1))