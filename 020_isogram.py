import string

def is_isogram(word):
    unique_chars = []
    
    for c in word:
        if c in string.ascii_letters:
            if c.lower() not in unique_chars:
                unique_chars.append(c.lower())
            else:
                return False
    
    return True

print(is_isogram('isograms'))
        