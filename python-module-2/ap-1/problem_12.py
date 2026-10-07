def match_up(a, b):
    """
    Given 2 arrays that are the same length containing strings, compare the 1st string in one array to the 1st string in the other array, the 2nd to the 2nd and so on. Count the number of times that the 2 strings are non-empty and start with the same char. The strings may be any length, including 0.


    match_up(["aa", "bb", "cc"], ["aaa", "xx", "bb"]) → 1
    match_up(["aa", "bb", "cc"], ["aaa", "b", "bb"]) → 2
    match_up(["aa", "bb", "cc"], ["", "", "ccc"]) → 1
    """

    count = 0

    for i in range(len(a)):
        if a[i] != "" and b[i] != "" and a[i][0] == b[i][0]:
            count += 1

    return count


print(match_up(["aa", "bb", "cc"], ["aaa", "xx", "bb"]))
print(match_up(["aa", "bb", "cc"], ["aaa", "b", "bb"]))
print(match_up(["aa", "bb", "cc"], ["", "", "ccc"]))