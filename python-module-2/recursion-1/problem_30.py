"""Recursion-1: str_dist problem solution."""


def str_dist(s: str, sub: str) -> int:
    """Return length of largest substring that starts and ends with sub.

    Args:
        s: Input string.
        sub: Non-empty target substring.

    Returns:
        Length of the largest substring starting and ending with sub.

    Complexity:
        Time Complexity: O(n^2) due to recursive prefix/suffix slicing.
        Space Complexity: O(n^2) auxiliary space for sliced strings.

    Examples:
        >>> str_dist("catcowcat", "cat")
        9
        >>> str_dist("catcowcat", "cow")
        3
        >>> str_dist("cccatcowcatxx", "cat")
        9
    """
    if len(s) < len(sub):
        return 0
    if not s.startswith(sub):
        return str_dist(s[1:], sub)
    if not s.endswith(sub):
        return str_dist(s[:-1], sub)
    return len(s)


if __name__ == "__main__":
    print(str_dist("catcowcat", "cat"))
    print(str_dist("catcowcat", "cow"))
    print(str_dist("cccatcowcatxx", "cat"))
