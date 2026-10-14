"""Recursion-1: nest_paren problem solution."""


def nest_paren(s: str) -> bool:
    """Return True if s is a nesting of zero or more pairs of parentheses.

    Args:
        s: Input string of parentheses.

    Returns:
        True if correctly nested parentheses, False otherwise.

    Complexity:
        Time Complexity: O(n^2) due to string slicing.
        Space Complexity: O(n^2) auxiliary space for sliced strings.

    Examples:
        >>> nest_paren("(())")
        True
        >>> nest_paren("((()))")
        True
        >>> nest_paren("(((x))")
        False
    """
    if not s:
        return True
    if s[0] == "(" and s[-1] == ")":
        return nest_paren(s[1:-1])
    return False


if __name__ == "__main__":
    print(nest_paren("(())"))
    print(nest_paren("((()))"))
    print(nest_paren("(((x))"))
