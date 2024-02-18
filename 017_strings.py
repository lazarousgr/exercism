"""
Provides some vocabulary functions
"""
import re


def add_prefix_un(word):
    return ''.join(['un', word])

def make_word_groups(vocab_words):
    array = [vocab_words[0]]
    for idx in range(1, len(vocab_words)):
        array.append(vocab_words[0] + vocab_words[idx])
        
    return ' :: '.join(array)

def remove_suffix_ness(word):
    return re.sub('i$', 'y', re.sub('ness$', '', word))

def adjective_to_verb(sentence, index):
    return re.sub('\\.$', '', sentence.split()[index]) + 'en'
    
    
print(adjective_to_verb('I need to make that bright.', -1))