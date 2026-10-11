"""String-2: cat_dog problem solution."""


def cat_dog(s: str) -> bool:
    """Return True if 'cat' and 'dog' appear the same number of times.

    Return True if the string "cat" and "dog" appear the same number of
    times in the given string.

    Args:
        s: The input string.

    Returns:
        True if count of "cat" equals count of "dog", False otherwise.

    Complexity:
        Time Complexity: O(N) where N is the length of the string.
        Space Complexity: O(1) auxiliary space.

    Examples:
        >>> cat_dog('catdog')
        True
        >>> cat_dog('catcat')
        False
        >>> cat_dog('1cat1cadodog')
        True
    """
    return s.count("cat") == s.count("dog")


if __name__ == "__main__":
    print(cat_dog("catdog"))
    print(cat_dog("catcat"))
    print(cat_dog("1cat1cadodog"))