def value_of_card(card):
    int_value = None
    
    if card in ['J', 'Q', 'K']:
        int_value = 10
    elif card == 'A':
        int_value = 1
    elif card in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
        int_value = int(card)
        
    return int_value
    
def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    
    return card_one, card_two
    
def value_of_ace(card_one, card_two):
    int_value = None
    
    if 'A' in [card_one,  card_two]:
        int_value = 1
    elif value_of_card(card_one) + value_of_card(card_two) + 11 < 22:
        int_value = 11
    else:
        int_value = 1
        
    return int_value
    
def is_blackjack(card_one, card_two):
    return (value_of_card(card_one) == 10 and value_of_card(card_two) == 1 or
       value_of_card(card_one) == 1 and value_of_card(card_two) == 10)
    

def can_split_pairs(card_one, card_two):   
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    return value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11]
