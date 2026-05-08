def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    i = number
    counter = 0
    while i != 1:
        counter = counter + 1
        if i % 2 == 0:
            i = i // 2
        else:
            i = i * 3 + 1
    return counter