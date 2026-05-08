def square(number):
    """Return the number of grains on a given square.
    The value is calculated as 2^(number - 1).
    Args:
        number (int): The square number (must be between 1 and 64).
    Returns:
        int: Number of grains on the given square.
    Raises:
        ValueError: If number is not between 1 and 64.
    """
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    """Return the total number of grains on the chessboard.
    This is the sum of grains on all 64 squares.
    Returns:
        int: Total number of grains.
    """
    return 2 * square(64) - 1
