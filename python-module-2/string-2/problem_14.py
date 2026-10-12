"""String-2: plus_out problem solution."""


def plus_out(s: str, word: str) -> str:
    """Replace all characters with '+' except preserved occurrences of word.

    Given a string and a non-empty word string, return a version of the
    original string where all chars have been replaced by pluses ("+"),
    except for appearances of the word string which are preserved.

    Args:
        s: The original input string.
        word: The non-empty word string to preserve.

    Returns:
        The masked string with preserved words and '+' everywhere else.

    Complexity:
        Time Complexity: O(len(s) * len(word)).
        Space Complexity: O(len(s)) to store the output string.

    Examples:
        >>> plus_out("12xy34", "xy")
        '++xy++'
        >>> plus_out("12xy34", "1")
        '1+++++'
        >>> plus_out("12xy34xyabcxy", "xy")
        '++xy++xy+++xy'
    """
    result = []
    i = 0
    w_len = len(word)
    while i < len(s):
        if s[i:i + w_len] == word:
            result.append(word)
            i += w_len
        else:
            result.append("+")
            i += 1
    return "".join(result)


if __name__ == "__main__":
    print(plus_out("12xy34", "xy"))
    print(plus_out("12xy34", "1"))
    print(plus_out("12xy34xyabcxy", "xy"))
