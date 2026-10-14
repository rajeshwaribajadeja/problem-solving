"""Map-2: first_swap problem solution."""


def first_swap(words: list) -> list:
    """Swap matching strings at most once per unique starting character.

    If a string matches an earlier string in the array, swap the two
    strings. A particular first character can only cause one swap; once
    a character has caused a swap, its later swaps are disabled.

    Args:
        words: List of non-empty strings.

    Returns:
        The list after performing first match swaps.

    Complexity:
        Time Complexity: O(n) where n is the number of words.
        Space Complexity: O(k) where k is the number of distinct initial
            characters.

    Examples:
        >>> first_swap(["ab", "ac"])
        ['ac', 'ab']
        >>> first_swap(["ax", "bx", "cx", "cy", "by", "ay", "aaa", "azz"])
        ['ay', 'by', 'cy', 'cx', 'bx', 'ax', 'aaa', 'azz']
        >>> first_swap(["ax", "bx", "ay", "by", "ai", "aj", "bx", "by"])
        ['ay', 'by', 'ax', 'bx', 'ai', 'aj', 'bx', 'by']
    """
    seen = {}
    disabled = set()
    for i in range(len(words)):
        first_char = words[i][0]
        if first_char in disabled:
            continue
        if first_char in seen:
            prev_idx = seen.pop(first_char)
            words[i], words[prev_idx] = words[prev_idx], words[i]
            disabled.add(first_char)
        else:
            seen[first_char] = i
    return words


if __name__ == "__main__":
    print(first_swap(["ab", "ac"]))
    print(first_swap(["ax", "bx", "cx", "cy", "by", "ay", "aaa", "azz"]))
    print(first_swap(["ax", "bx", "ay", "by", "ai", "aj", "bx", "by"]))