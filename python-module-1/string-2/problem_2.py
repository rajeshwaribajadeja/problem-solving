def count_hi(str):
    """
    Return the number of times that the string "hi" appears in the given string.

    count_hi('abc hi ho') → 1
    count_hi('ABChi hi') → 2
    count_hi('hihi') → 2
    """

    # return str.count("hi")

    count = 0
    for i in range(len(str) - 1):
        if str[i:i+2] == "hi":
            count += 1
    return count

print(count_hi('abc hi ho'))
print(count_hi('ABChi hi'))
print(count_hi('hihi'))
