def count_triple(str):
    """
    We'll say that a "triple" in a string is a char appearing three times in a row. Return the number of triples in the given string. The triples may overlap.


    count_triple("abcXXXabc") → 1
    count_triple("xxxabyyyycd") → 3
    count_triple("a") → 0
    """

    count = 0
    for i in range(len(str)-2):
        if str[i] == str[i+1] == str[i+2]:
            count += 1

    return count

print(count_triple("abcXXXabc"))
print(count_triple("xxxabyyyycd"))
print(count_triple("a"))