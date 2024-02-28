def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    str = ''  
    
    for char in text:
        idx = alphabet.find(char)
        if 0 <= idx <= 25:
           str += alphabet[(idx+key)%26]
        elif idx > 25:
            str += alphabet[(idx+key)%26 + 26]
        else:
            str += char
    
    
    return str

print(rotate('Let\'s eat, Grandma!', 21))
            