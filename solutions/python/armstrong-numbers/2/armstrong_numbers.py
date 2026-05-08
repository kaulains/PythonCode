"""
Check if a number is an Armstrong (narcissistic) number.
"""  
def is_armstrong_number(number):
    """
    An Armstrong number is a number that is equal to the sum of its digits,
    each raised to the power of the number of digits.

    Examples:
        is_armstrong_number(153) -> True   # 1^3 + 5^3 + 3^3 = 153
        is_armstrong_number(9474) -> True  # 9^4 + 4^4 + 7^4 + 4^4 = 9474
        is_armstrong_number(123) -> False

    :param number: int - The number to check
    :return: bool - True if Armstrong number, otherwise False
    """
    digits = str(number)
    power = len(digits)
    total = 0
    
    for digit in digits:
        total += int(digit) ** power
    return total == number   

 
        
        
