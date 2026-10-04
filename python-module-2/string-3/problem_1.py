def count_yz(str):
    """
    Given a string, count the number of words ending in 'y' or 'z' -- so the 'y' in "heavy" and the 'z' in "fez" count, but not the 'y' in "yellow" (not case sensitive). We'll say that a y or z is at the end of a word if there is not an alphabetic letter immediately following it. 


    count_yz("fez day") → 2
    count_yz("day fez") → 2
    count_yz("day fyyyz") → 2
    """
    count = 0

    for i in range(len(str)):
        if str[i].lower() == 'y' or str[i].lower() == 'z':
            if i == len(str) - 1 or not str[i + 1].isalpha():
                count += 1

    return count

print(count_yz("fez day"))
print(count_yz("day fez"))
print(count_yz("day fyyyz"))