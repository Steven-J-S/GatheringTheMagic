"""
This module contains some utility functions for the game

todo: move play() and cast() functions to player?
"""

import json
import os
from game.card import Card
from game.creature import Creature
from game.land import Land
from game.instant import Instant
from game.sorcery import Sorcery


def load_deck(file):
    """Main logic to load a deck (hard coded)"""
    with open('Decks/'+file+'.json', 'r', encoding='utf-8-sig') as f:
        deck = json.load(f)
    return deck['mainBoard']


def build_deck(lst):
    """Logic to build deck into list of card objects"""
    deck = []
    for c in lst:
        if c['types'][0] == 'Creature': card = Creature(c)
        elif c['types'][0] == 'Land': card = Land(c)
        elif c['types'][0] == 'Instant': card = Instant(c)
        elif c['types'][0] == 'Sorcery': card = Sorcery(c)
        # Add more card types
        else: card = Card(c)
        deck.append(card)
    return deck


def clear_command_line():
    os.system('cls')


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
