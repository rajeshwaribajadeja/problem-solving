"""Map-2: all_swap problem solution."""


def all_swap(words: list) -> list:
    """Swap matching strings whose first characters match earlier unseen
    strings.

    If a string matches an earlier string with the same first character,
    swap the two strings in the array. When a position has been swapped,
    it no longer matches anything.

    Args:
        words: List of non-empty strings.

    Returns:
        The list after performing all match swaps.

    Complexity:
        Time Complexity: O(n) where n is the number of words.
        Space Complexity: O(k) where k is the number of distinct initial
            characters.

    Examples:
        >>> all_swap(["ab", "ac"])
        ['ac', 'ab']
        >>> all_swap(["ax", "bx", "cx", "cy", "by", "ay", "aaa", "azz"])
        ['ay', 'by', 'cy', 'cx', 'bx', 'ax', 'azz', 'aaa']
        >>> all_swap(["ax", "bx", "ay", "by", "ai", "aj", "bx", "by"])
        ['ay', 'by', 'ax', 'bx', 'aj', 'ai', 'by', 'bx']
    """
    seen = {}
    for i in range(len(words)):
        first_char = words[i][0]
        if first_char in seen:
            prev_idx = seen.pop(first_char)
            words[i], words[prev_idx] = words[prev_idx], words[i]
        else:
            seen[first_char] = i
    return words


if __name__ == "__main__":
    print(all_swap(["ab", "ac"]))
    print(all_swap(["ax", "bx", "cx", "cy", "by", "ay", "aaa", "azz"]))
    print(all_swap(["ax", "bx", "ay", "by", "ai", "aj", "bx", "by"]))