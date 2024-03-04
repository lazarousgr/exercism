def reverse(text):
    
    rev_text = ''
    
    for n in reversed(range(len(text))):
        rev_text += text[n]
        
    return rev_text

print(reverse(''))