def square(number):
    """Square function is calculation 
    number in square"""
    if 1 <= number <= 64:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    """Calculation total 
    value in board"""
    return 2 * square(64) -1 
