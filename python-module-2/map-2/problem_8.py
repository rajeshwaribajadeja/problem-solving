def all_swap(words):
    """
    We'll say that 2 strings "match" if they are non-empty and their first chars are the same. Loop over and then return the given array of non-empty strings as follows: if a string matches an earlier string in the array, swap the 2 strings in the array. When a position in the array has been swapped, it no longer matches anything. Using a map, this can be solved making just one pass over the array. More difficult than it looks.



    all_swap(["ab", "ac"]) → ["ac", "ab"]
    all_swap(["ax", "bx", "cx", "cy", "by", "ay", "aaa", "azz"])
        → ["ay", "by", "cy", "cx", "bx", "ax", "azz", "aaa"]
    all_swap(["ax", "bx", "ay", "by", "ai", "aj", "bx", "by"])
        → ["ay", "by", "ax", "bx", "aj", "ai", "by", "bx"]
    """

    result = {}
    
    for i in range(len(words)):
        first_char = words[i][0]

        if first_char in result:
            previous_index = result[first_char]

            words[i], words[previous_index] = words[previous_index], words[i]

            result.pop(first_char)
        else:
            result[first_char] = i

    return words


print(all_swap(["ab", "ac"]))
print(all_swap(["ax", "bx", "cx", "cy", "by", "ay", "aaa", "azz"]))
print(all_swap(["ax", "bx", "ay", "by", "ai", "aj", "bx", "by"]))