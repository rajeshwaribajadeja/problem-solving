
def max_block(str):
    """
    Given a string, return the length of the largest "block" in the string.
    A block is a run of adjacent chars that are the same.

    max_block("hoopla") → 2
    max_block("abbCCCddBBBxx") → 3
    max_block("") → 0
    """

    if len(str) == 0:
        return 0

    max_len = 1
    block_len = 1

    for i in range(1, len(str)):
        if str[i] == str[i - 1]:
            block_len += 1
        else:
            block_len = 1

        if block_len > max_len:
            max_len = block_len

    return max_len


print(max_block("hoopla"))
print(max_block("abbCCCddBBBxx"))
print(max_block(""))