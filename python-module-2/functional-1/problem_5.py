"""Functional-1: more_y problem solution."""


def more_y(words: list) -> list:
    """Return a list where each string has 'y' added at its start and end.

    Args:
        words: List of strings.

    Returns:
        List of strings surrounded by 'y'.

    Complexity:
        Time Complexity: O(n * L) where n is the number of words and L is
            the average string length.
        Space Complexity: O(n * L) for the newly created output list.

    Examples:
        >>> more_y(["a", "b", "c"])
        ['yay', 'yby', 'ycy']
        >>> more_y(["hello", "there"])
        ['yhelloy', 'ytherey']
        >>> more_y(["yay"])
        ['yyayy']
    """

    return list(map(lambda x: "y" + x + "y", words))


if __name__ == "__main__":
    print(more_y(["a", "b", "c"]))
    print(more_y(["hello", "there"]))
    print(more_y(["yay"]))
