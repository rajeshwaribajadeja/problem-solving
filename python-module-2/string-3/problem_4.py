def g_happy(str):
    """We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right. Return true if all the g's in the given string are happy.


    g_happy("xxggxx") → true
    g_happy("xxgxx") → false
    g_happy("xxggyygxx") → false
    """

    for i in range(len(str)):
        if str[i] == 'g':
            if (i == 0 or str[i - 1] != 'g') and (i == len(str) - 1 or str[i + 1] != 'g'):
                return False
    return True

print(g_happy("xxggxx"))
print(g_happy("xxgxx"))
print(g_happy("xxggyygxx"))