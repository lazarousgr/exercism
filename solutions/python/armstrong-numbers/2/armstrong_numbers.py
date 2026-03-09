def is_armstrong_number(number):
    digits = [int(idx) for idx in str(number)]

    out = []
    no_digits = len(digits)
    for idx in range(no_digits):
        out.append(digits[idx] ** no_digits)
    
    print(out)

    return number == sum(out)
print(is_armstrong_number(153))