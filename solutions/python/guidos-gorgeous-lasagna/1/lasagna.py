EXPECTED_BAKE_TIME=40
EXPECTED_LAYER_BAKE_TIME=2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the total preparation time.

    :param number_of_layers: int - number of lasagna layers to prepare.
    :return: int - total preparation time (in minutes) based on layer count.
    """
    return number_of_layers * EXPECTED_LAYER_BAKE_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed cooking time.

    :param number_of_layer: int - number of prepared lasagna layers.
    :param elapsed_bake_time: int - time already spent baking.
    :return: int - combined preparation and elapsed bake time (in minutes).
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time 
