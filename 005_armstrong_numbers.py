def is_armstrong_number(number):
    number_length = len("%i" % number)
       
    armstrong_number_wannabe = 0
    remainder_number = number
    
    for i in range(0, number_length):
        armstrong_number_wannabe += pow((remainder_number % 10), number_length)
        remainder_number = remainder_number // 10
        
    return armstrong_number_wannabe == number
    
print(is_armstrong_number(153))
