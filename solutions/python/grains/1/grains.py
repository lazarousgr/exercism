def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return number
    else:
        return square(number-1) * 2


def total():
    total = 0;
    for i in range(64):
        total += square(i + 1)
    
    return total