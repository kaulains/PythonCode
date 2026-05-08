def leap_year(year):
    """
    Determine whether a given year is a leap year.

    A leap year follows these rules:
    - It must be divisible by 4
    - If it is divisible by 100, it is NOT a leap year
    - Unless it is also divisible by 400, in which case it IS a leap year

    Examples:
        leap_year(2000) -> True
        leap_year(1900) -> False
        leap_year(2024) -> True
        leap_year(2023) -> False

    :param year: int - The year to check
    :return: bool - True if leap year, otherwise False
    """
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
