"""String-3: count_yz problem solution."""


def count_yz(s: str) -> int:
    """Count the number of words ending in 'y' or 'z' (case-insensitive).

    Given a string, count the number of words ending in 'y' or 'z' -- so
    the 'y' in "heavy" and the 'z' in "fez" count, but not the 'y' in
    "yellow" (not case sensitive). A y or z is at the end of a word if
    there is not an alphabetic letter immediately following it.

    Args:
        s: The input string.

    Returns:
        The count of words ending with 'y' or 'z'.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> count_yz("fez day")
        2
        >>> count_yz("day fez")
        2
        >>> count_yz("day fyyyz")
        2
    """
    count = 0
    for i in range(len(s)):
        if s[i].lower() in ("y", "z"):
            if i == len(s) - 1 or not s[i + 1].isalpha():
                count += 1
    return count


if __name__ == "__main__":
    print(count_yz("fez day"))
    print(count_yz("day fez"))
    print(count_yz("day fyyyz"))