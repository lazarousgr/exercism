"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    words = title.split()
    
    for i in range(0, len(words)) :
        words[i] = words[i].title()
        
    return ' '.join(words)


def check_sentence_ending(sentence):
    return sentence.endswith('.')


def clean_up_spacing(sentence):
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    sentence.replace(old_word, new_word)
