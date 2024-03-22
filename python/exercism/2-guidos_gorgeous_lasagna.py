""" Guido's Gorgeous Lasagna """
EXPECTED_BAKE_TIME = 40

def bake_time_remaining(time_passed):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - time_passed

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time according to the number of layers

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total time elapsed (in minutes) preparing.

    The preparation_time_in_minutes(number_of_layers) function takes 
    the number of layers you want to add to the lasagna as an argument and returns 
    how many minutes you would spend making them. Assume each layer takes 2 minutes to prepare.
    """
    return 2*number_of_layers


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
