"""Module for calculating grains on a chessboard using powers of 2."""

def square(number):
    """Return the number of grains on a given square."""
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    """Return the total number of grains on the chessboard."""
    return 2 * square(64) - 1