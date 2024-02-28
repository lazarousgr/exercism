import re

def is_valid(isbn):

    match = re.match('^[0-9]{1}-[0-9]{3}-[0-9]{5}-([0-9]|X)$|^[0-9]{10}$|^[0-9]{9}X$', isbn)
    
    if not match:
        return False
    
    isbn_digits = [int(s) for s in isbn if s.isdigit()]
    if isbn.endswith('X'):
        isbn_digits.append(10)
                 
    sum = 0
    for idx in range(len(isbn_digits)):
        sum += isbn_digits[idx] * (10 - idx)
         
    return sum % 11 == 0

print(is_valid('98245726788'))