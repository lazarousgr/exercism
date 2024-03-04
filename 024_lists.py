def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    total = 0
    for value in hand:
        total += value

    return total/len(hand)

def approx_average_is_average(hand):
    """Return if an average is using (first + last index values )
    OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    average = card_average(hand)
    if average == (hand[0] + hand[len(hand)-1])/2:
        return True
    if average == hand[ len(hand) // 2 ]:
        return True
    return False

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    odd_numbers = []
    even_numbers = []

    for idx, value in enumerate(hand):
        if idx % 2 == 0:
            odd_numbers.append(value)
        else:
            even_numbers.append(value)

    return card_average(odd_numbers) ==  card_average(even_numbers)

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    last_elm = hand[len(hand) - 1]
    if last_elm == 11:
        hand[len(hand) - 1] = 22

    return hand

print(average_even_is_average_odd([1, 3, 5, 7, 9]))
