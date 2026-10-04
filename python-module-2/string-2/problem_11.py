def one_two(str):
    """
    Given a string, compute a new string by moving the first char to come after the next two chars, so "abc" yields "bca". Repeat this process for each subsequent group of 3 chars, so "abcdef" yields "bcaefd". Ignore any group of fewer than 3 chars at the end.


    one_two("abc") → "bca"
    one_two("tca") → "cat"
    one_two("tcagdo") → "catdog"
    """
    result = ""
    for i in range(0, len(str) - 2, 3):
        result = result + str[i + 1: i + 3] + str[i]
    return result

print(one_two("abc"))
print(one_two("tca"))
print(one_two("tcagdo"))
    
