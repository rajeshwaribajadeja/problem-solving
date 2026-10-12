"""String-2: bob_there problem solution."""


def bob_there(s: str) -> bool:
    """Return True if the string contains 'b?b' where ? can be any char.

    Given a string, return True if it contains a "bob" string, but where
    the middle 'o' char can be any character.

    Args:
        s: The input string.

    Returns:
        True if any 'b?b' pattern is present, False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> bob_there("abcbob")
        True
        >>> bob_there("b9b")
        True
        >>> bob_there("bac")
        False
    """
    return any(s[i] == "b" and s[i + 2] == "b" for i in range(len(s) - 2))


if __name__ == "__main__":
    print(bob_there("abcbob"))
    print(bob_there("b9b"))
    print(bob_there("bac"))