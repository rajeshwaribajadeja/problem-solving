"""Recursion-1: change_xy problem solution."""


def change_xy(s: str) -> str:
    """Return a new string where all lowercase 'x' are changed to 'y'.

    Args:
        s: Input string.

    Returns:
        String with 'x' replaced by 'y'.

    Complexity:
        Time Complexity: O(n^2) due to string slicing and concatenation.
        Space Complexity: O(n^2) auxiliary space for string construction.

    Examples:
        >>> change_xy("codex")
        'codey'
        >>> change_xy("xxhixx")
        'yyhiyy'
        >>> change_xy("xhixhix")
        'yhiyhiy'
    """
    if not s:
        return ""
    char = "y" if s[0] == "x" else s[0]
    return char + change_xy(s[1:])


if __name__ == "__main__":
    print(change_xy("codex"))
    print(change_xy("xxhixx"))
    print(change_xy("xhixhix"))
