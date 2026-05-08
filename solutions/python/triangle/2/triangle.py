"""
Triangle classification module.

This module provides utilities to determine whether a set of three side lengths
forms a valid triangle, and to classify it as:
- Equilateral
- Isosceles
- Scalene

All functions assume input is an iterable of three numeric side lengths.
"""

def is_valid_triangle(triangle_sides):
    """
    Check whether three side lengths can form a valid triangle.

    A valid triangle must satisfy:
    - All sides are greater than 0
    - Triangle inequality theorem:
      the sum of any two sides must be greater than or equal to the third

    Args:
        triangle_sides (list or tuple of float/int): Three side lengths.

    Returns:
        bool: True if valid triangle, False otherwise.
    """
    return (
        all(side > 0 for side in triangle_sides) and
        triangle_sides[0] + triangle_sides[1] >= triangle_sides[2] and
        triangle_sides[1] + triangle_sides[2] >= triangle_sides[0] and
        triangle_sides[0] + triangle_sides[2] >= triangle_sides[1]
    )


def equilateral(triangle_sides):
    """
    Determine if a triangle is equilateral.

    A triangle is equilateral if:
    - It is a valid triangle
    - All three sides are equal

    Args:
        triangle_sides (list or tuple of float/int): Three side lengths.

    Returns:
        bool: True if equilateral triangle, False otherwise.
    """
    return is_valid_triangle(triangle_sides) and triangle_sides[0] == triangle_sides[1] == triangle_sides[2]


def isosceles(triangle_sides):
    """
    Determine if a triangle is isosceles.

    A triangle is isosceles if:
    - It is a valid triangle
    - At least two sides are equal

    Note:
        Equilateral triangles are also considered isosceles.

    Args:
        triangle_sides (list or tuple of float/int): Three side lengths.

    Returns:
        bool: True if isosceles triangle, False otherwise.
    """
    return (
        is_valid_triangle(triangle_sides)
        and (
            triangle_sides[0] == triangle_sides[1]
            or triangle_sides[0] == triangle_sides[2]
            or triangle_sides[1] == triangle_sides[2]
        )
    )


def scalene(triangle_sides):
    """
    Determine if a triangle is scalene.

    A triangle is scalene if:
    - It is a valid triangle
    - All sides are different

    Args:
        triangle_sides (list or tuple of float/int): Three side lengths.

    Returns:
        bool: True if scalene triangle, False otherwise.
    """
    return (
        is_valid_triangle(triangle_sides)
        and triangle_sides[0] != triangle_sides[1]
        and triangle_sides[0] != triangle_sides[2]
        and triangle_sides[1] != triangle_sides[2]
    )