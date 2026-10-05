def first_swap(words):
    """
    We'll say that 2 strings "match" if they are non-empty and their first chars are the same. Loop over and then return the given array of non-empty strings as follows: if a string matches an earlier string in the array, swap the 2 strings in the array. A particular first char can only cause 1 swap, so once a char has caused a swap, its later swaps are disabled. Using a map, this can be solved making just one pass over the array. More difficult than it looks.


    first_swap(["ab", "ac"]) → ["ac", "ab"]
    first_swap(["ax", "bx", "cx", "cy", "by", "ay", "aaa", "azz"])
        → ["ay", "by", "cy", "cx", "bx", "ax", "aaa", "azz"]
    first_swap(["ax", "bx", "ay", "by", "ai", "aj", "bx", "by"])
        → ["ay", "by", "ax", "bx", "ai", "aj", "bx", "by"]
    """

    result = {}
    used = set()

    for i in range(len(words)):
        first_char = words[i][0]

        # Skip if this character has already caused a swap
        if first_char in used:
            continue

        if first_char in result:
            previous_index = result[first_char]

            words[i], words[previous_index] = words[previous_index], words[i]

            # Character has now used its one allowed swap
            result.pop(first_char)
            used.add(first_char)

        else:
            result[first_char] = i

    return words


print(first_swap(["ab", "ac"]))
print(first_swap(["ax", "bx", "cx", "cy", "by", "ay", "aaa", "azz"]))
print(first_swap(["ax", "bx", "ay", "by", "ai", "aj", "bx", "by"]))