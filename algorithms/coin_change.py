from typing import Dict, Tuple

def coin_change(cents: int) -> Tuple[int, Dict[str, int]]:
    """Returns the number of coins required for an amount of change"""
    coins = [5, 2, 1, 0.5, 0.2, 0.1]
    count = 0
    used_coins = {'5': 0, '2': 0, '1': 0, '0.5': 0}
    for coin in coins:
        while cents >= coin:
            used_coins[str(coin)] += 1
            cents -= coin
            count += 1
    return count, used_coins


def notes_change(value: int) -> Tuple[int, Dict[str, int]]:
    """Returns change in notes for a specific amount"""
    if value%10 != 0:
        raise ValueError("Value must be multiple of 10")
    notes = [200, 100, 50, 20, 10]
    notes_count = 0
    used_notes = {"200": 0, "100": 0, "50": 0, "20": 0, "10": 0}
    for note in notes:
        while value >= note:
            used_notes[str(note)] += 1
            value -= note
            notes_count += 1
    return notes_count, used_notes


def all_change(value: int) -> Tuple[int, Dict[str, int]]:
    """Returns change of any amount using a combination of notes & coins"""
    denominations = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1]
    count = 0
    used_denominations = {
                        "200": 0, "100": 0, "50": 0, "20": 0, "10": 0,
                        "5": 0, "2": 0, "1": 0, "0.5": 0, "0.2": 0, "0.1": 0
                        }
    for denomination in denominations:
        while value >= denomination:
            used_denominations[str(denomination)] += 1
            value -= denomination
            count += 1

    # delete unused denomination from used_denominations
    for denomination in denominations:
        if used_denominations[str(denomination)] == 0:
            del used_denominations[str(denomination)]

    return count, used_denominations


print(all_change(1060.53))
