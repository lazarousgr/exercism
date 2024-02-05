def steps(number):
    
    no_of_steps = 0
    
    if number < 1:
        raise ValueError("Only positive integers are allowed")

    while number != 1:
        if (number % 2) == 0:
            no_of_steps += 1
            number /= 2
        else:
            no_of_steps += 1
            number = 3 * number + 1
    
    return no_of_steps

print(steps(12))