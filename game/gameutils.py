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


def load_cards():
    """Main logic to load all cards"""
    with open('Cards/AllCards.json', 'r', encoding='utf-8-sig') as f:
        cards = json.load(f)
    return cards


def make_deck(lst):
    """Logic to build deck into list of card objects"""
    deck = list()
    for c in lst:
        if c['types'][0] == 'Creature': card = Creature(c)
        elif c['types'][0] == 'Land': card = Land(c)
        elif c['types'][0] == 'Instant': card = Instant(c)
        elif c['types'][0] == 'Sorcery': card = Sorcery(c)
        # Add more card types
        else: card = Card(c)
        deck.append(card)
    return deck


def build_deck():
    """Logic to build a deck from cards"""
    clear_command_line()
    cards = load_cards()
    lst = list()
    choice = None
    while choice != 'q':
        choice = str(input('Pick a card to add to deck: (input: q to quit, s to search)'))
        if choice == 'q':
            break
        elif choice == 's':
            card = search_card(cards)
        else:
            card = cards[choice]
        amount = int(input('How many copies do you want to add to deck: '))
        for i in range(amount):
            lst.append(card)
        clear_command_line()
    deck = make_deck(lst)
    return deck


def search_card(cards):
    """Logic to search card"""
    keys = list(cards.keys())
    choice = 's'
    while choice == 's':
        search = str(input('Search card containing in title: ...'))
        for k in keys:
            if search in k:
                print(k)
        choice = str(input('Pick a card from list: (enter s to search again)'))
    card = cards[choice]
    return card



def print_bold(text):
    """Logic to print text in bold"""
    print('\033[1m' + str(text) + '\033[0m')


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
