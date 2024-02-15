def classify(number):
    if number <= 0 or number != int(number):
        raise ValueError("Classification is only possible for positive integers.")
    
    
    total_sum = 0
    for i in range(1, number):
        if number % i == 0:
            total_sum += i
    
    if(total_sum == number):
        return 'perfect'
    elif(total_sum > number):
        return 'abundant'
    else:
        return 'deficient'
    
print(classify(33550337))