"""Functions for calculating steps in exchanging currency."""

def exchange_money(budget, exchange_rate):
    """
    Return the exchanged value of the foreign currency.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Return the amount left after exchanging `exchanging_value`.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Return total value of bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    Return number of whole bills obtainable.
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """
    Return leftover amount after exchanging bills.
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum exchangeable value in whole bills.
    """
    # Spread converts percentage to effective exchange rate
    rate_with_spread = exchange_rate * (1 + spread / 100)

    # Get amount after exchange
    exchanged_amount = budget / rate_with_spread

    # Number of whole bills we can get
    bills = int(exchanged_amount // denomination)

    # Return total bill value
    return bills * denomination
