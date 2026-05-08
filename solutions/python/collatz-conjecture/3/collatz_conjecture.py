def steps(number):
    """implementing the Collatz conjecture"""
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    result = number
    counter = 0
    while result != 1:
        counter = counter + 1
        if result % 2 == 0:
            result = result // 2
        else:
            result = result * 3 + 1
    return counter