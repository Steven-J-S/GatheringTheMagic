"""
This module contains the deck class

todo: add shuffle logic
todo: add take logic
todo: add pick logic
todo: add logic to end game if deck of cards is empty
todo: add logic to search the deck given a string
todo: make a deck type superclass for deck and graveyard and exile and hand
todo: add logic in put() function to put anywhere in the deck (top, bottom)
"""

from deck import Deck
from random import shuffle


class Library(Deck):
    """Class to represent a players library"""
    def __init__(self, lst=[]):
        Deck.__init__(self, lst=lst)
        self.shuffle()
        self.visible = False

    def shuffle(self):
        shuffle(self.cards)
