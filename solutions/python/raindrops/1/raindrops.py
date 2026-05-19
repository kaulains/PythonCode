"""
Convert a number into a raindrop sound string.
"""
def convert(number):
    """
    Rules:
    - If the number is divisible by 3, add "Pling" to the result.
    - If the number is divisible by 5, add "Plang" to the result.
    - If the number is divisible by 7, add "Plong" to the result.
    - If the number is not divisible by 3, 5, or 7,
      return the number as a string.
    """
    result = ''

    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"

    if result == '':
        result = str(number)

    return result
