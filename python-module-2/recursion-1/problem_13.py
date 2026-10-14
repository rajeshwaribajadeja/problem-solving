"""Recursion-1: change_pi problem solution."""


def change_pi(s: str) -> str:
    """Return a new string where all occurrences of 'pi' become '3.14'.

    Args:
        s: Input string.

    Returns:
        String with 'pi' replaced by '3.14'.

    Complexity:
        Time Complexity: O(n^2) due to string slicing and concatenation.
        Space Complexity: O(n^2) auxiliary space for string construction.

    Examples:
        >>> change_pi("xpix")
        'x3.14x'
        >>> change_pi("pipi")
        '3.143.14'
        >>> change_pi("pip")
        '3.14p'
    """
    if len(s) < 2:
        return s
    if s[:2] == "pi":
        return "3.14" + change_pi(s[2:])
    return s[0] + change_pi(s[1:])


if __name__ == "__main__":
    print(change_pi("xpix"))
    print(change_pi("pipi"))
    print(change_pi("pip"))
