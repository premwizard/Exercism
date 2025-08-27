"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This module contains functions to calculate the baking time,
preparation time, and total elapsed cooking time for lasagna.
"""

EXPECTED_BAKE_TIME = 40  
PREPARATION_TIME = 2     


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes).

    This function takes the actual minutes the lasagna has been in the oven
    as an argument and returns how many minutes the lasagna still needs to
    bake based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time.

    :param number_of_layers: int - the number of lasagna layers being prepared.
    :return: int - total preparation time (in minutes).

    This function multiplies the number of layers by the
    preparation time per layer (PREPARATION_TIME).
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate total elapsed cooking time.

    :param number_of_layers: int - the number of lasagna layers prepared.
    :param elapsed_bake_time: int - the number of minutes the lasagna has already baked.
    :return: int - total elapsed cooking time (in minutes).

    This function returns the total time spent preparing and baking
    the lasagna up to now.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
