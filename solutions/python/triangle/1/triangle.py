def is_valid_triangle(sides):
    """
    Check whether three side lengths can form a valid triangle.

    A valid triangle must satisfy:
    - All sides are greater than 0
    - Triangle inequality theorem:
      sum of any two sides must be greater than or equal to the third

    Args:
        sides (list or tuple of float/int): Three side lengths.

    Returns:
        bool: True if valid triangle, False otherwise.
    """
    return (
        all(s > 0 for s in sides) and
        sides[0] + sides[1] >= sides[2] and
        sides[1] + sides[2] >= sides[0] and
        sides[0] + sides[2] >= sides[1]
    )


def equilateral(sides):
    """
    Determine if a triangle is equilateral.

    A triangle is equilateral if:
    - It is a valid triangle
    - All three sides are equal

    Args:
        sides (list or tuple of float/int): Three side lengths.

    Returns:
        bool: True if equilateral triangle, False otherwise.
    """
    return is_valid_triangle(sides) and sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """
    Determine if a triangle is isosceles.

    A triangle is isosceles if:
    - It is a valid triangle
    - At least two sides are equal

    Note:
        Equilateral triangles are also considered isosceles.

    Args:
        sides (list or tuple of float/int): Three side lengths.

    Returns:
        bool: True if isosceles triangle, False otherwise.
    """
    return (
        is_valid_triangle(sides)
        and (sides[0] == sides[1] or
             sides[0] == sides[2] or
             sides[1] == sides[2])
    )


def scalene(sides):
    """
    Determine if a triangle is scalene.

    A triangle is scalene if:
    - It is a valid triangle
    - All sides are different

    Args:
        sides (list or tuple of float/int): Three side lengths.

    Returns:
        bool: True if scalene triangle, False otherwise.
    """
    return (
        is_valid_triangle(sides)
        and sides[0] != sides[1]
        and sides[0] != sides[2]
        and sides[1] != sides[2]
    )