def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    if number == 1:
        return number
    
    return square(number-1) * 2


def total():
    temp_sum = 0
    for number in range(64):
        temp_sum += square(number + 1)
    
    return temp_sum