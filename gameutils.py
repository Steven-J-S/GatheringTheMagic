"""
This module contains some utility functions for the game

todo: move play() and cast() functions to player?
"""

import json
from card import Card


def load_deck(file):
    """Main logic to load a deck (hard coded)"""
    with open('Decks/'+file+'.json', 'r', encoding='utf-8-sig') as f:
        deck = json.load(f)
    return deck['mainBoard']


def build_deck(lst):
    """Logic to build deck into list of card objects"""
    deck = []
    for c in lst:
        card = Card(c)
        deck.append(card)
    return deck


def check_health(obj):
    """Main logic to check the health of player or creature"""
    pass


def count_cards(obj, max):
    """Main logic to check the count of cards in hand of player"""
    pass


def play(obj):
    """Main logic to play a card"""
    pass


def cast(obj):
    """Main logic to cast a spell"""
    pass


def count_permanents(obj):
    """Main logic to count the permanents in the territory of a player"""
    pass


def inspect_graveyard(obj):
    """Main logic to inspect the graveyard of a person"""
    pass
