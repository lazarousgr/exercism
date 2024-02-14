def isvowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    synthetic_vowels = ['xr', 'yt']
    
    first_letter = word[0]
    two_first_letters = word[0:2]
    if first_letter in vowels:
        return True
    elif two_first_letters in synthetic_vowels:
        return True
    else:
        return False
    
def isconsonantchar(word):
    position = -1
    quy_found = False
    
    while position < len(word) and not quy_found:       
        if not isvowel(word[position+1:]):
            if word[position+2:].startswith('y'):
                quy_found = True
            elif word[position+2:].startswith('qu'):
                #position += 1
                quy_found = True
            position += 1
        else:
            quy_found = True
    
    return position

def isconsonant(text, position):
    ay = 'ay'
    qu = 'qu'
    y = 'y'
    
    if(position > -1):
        consonat_word = text[0:(position+1)]
        after_consonat_word = text[position+1:]
    
        ### Rule 3           
        if after_consonat_word.startswith(qu):
            return after_consonat_word[2:] + consonat_word + qu + ay
        ### Rule 4
        elif after_consonat_word.startswith(y):
            return after_consonat_word + consonat_word + ay
        ### Rule 2
        else:
            return after_consonat_word + consonat_word + ay
    return text
        

def translate(text):
    translation = ''
    
    list = text.split()
           
    
    for i in range(0, len(list)):
        element= list[i]
        
        if isvowel(element):
            list[i] += 'ay'
        elif element.startswith('qu'):
            list[i] = element[2:] + element[0:2] + 'ay'
        ##elif element.startswith('y'):
        ##    list[i] =  element[1:] + element[0:1] + 'ay'
        else:
           list[i] = isconsonant(element, isconsonantchar(element))
    
    return " ".join(list)
        


# print(translate("square"))
# print(translate("queen"))
# print(translate("yellow"))
# print(translate("quick fast run"))
print(translate("my"))
