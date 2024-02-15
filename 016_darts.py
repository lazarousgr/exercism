import math


def score(x, y):
    distance = math.sqrt(x**2 + y**2)
    
    if 0 <= distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    
    return 0
    
print(score(0, 10))