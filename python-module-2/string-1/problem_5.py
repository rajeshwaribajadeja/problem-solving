"""String-1: endsly problem solution."""


def endsly(s: str) -> bool:
    """Return True if the given string ends in 'ly'.

    Given a string, return True if it ends in "ly".

    Args:
        s: The input string.

    Returns:
        True if s ends with "ly", False otherwise.

    Complexity:
        Time Complexity: O(1) (checks suffix of length 2).
        Space Complexity: O(1)

    Examples:
        >>> endsly("oddly")
        True
        >>> endsly("y")
        False
        >>> endsly("oddy")
        False
    """
    return s[-2:] == "ly"

    
if __name__ == "__main__":
    print(endsly("oddly"))
    print(endsly("y"))
    print(endsly("oddy"))