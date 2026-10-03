def countxx(str):
    """
    Count the number of "xx" in the given string. We'll say that overlapping is allowed, so "xxx" contains 2 "xx".


    countXX("abcxx") → 1
    countXX("xxx") → 2
    countXX("xxxx") → 3

    """
    count = 0
    for i in range(len(str)-1):
        if str[i] == str[i+1] == "x":
            count += 1

    return count

print(countxx("abcxx"))
print(countxx("xxx"))
print(countxx("xxxx"))