"""String-1: make_out_word problem solution."""


def make_out_word(out: str, word: str) -> str:
    """Insert a word in the middle of a 4-character outer string.

    Given an "out" string of length 4, such as "<<>>", and a word,
    return a new string where the word is in the middle of the out
    string, e.g. "<<word>>".

    Args:
        out: The 4-character outer boundary string.
        word: The word to insert in the middle.

    Returns:
        The composite string with word placed inside out.

    Complexity:
        Time Complexity: O(len(word)) (since len(out) is fixed at 4).
        Space Complexity: O(len(word)) to store the resulting string.

    Examples:
        >>> make_out_word('<<>>', 'Yay')
        '<<Yay>>'
        >>> make_out_word('<<>>', 'WooHoo')
        '<<WooHoo>>'
        >>> make_out_word('[[]]', 'word')
        '[[word]]'
    """
    return out[:2] + word + out[2:]


if __name__ == "__main__":
    print(make_out_word("<<>>", "Yay"))
    print(make_out_word("<<>>", "WooHoo"))
    print(make_out_word("[[]]", "word"))
