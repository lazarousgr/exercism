def is_pangram(sentence):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    
    for char in sentence:
        letters = letters.replace(char.lower(), '')
        
    return True if len(letters) < 1 else False

print(is_pangram('abcdefghijklmnopqrstuvwxyz'))