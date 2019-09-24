"""
This module contains the hand class
"""

from game.deck import Deck


class Hand(Deck):
    """Class to represent the hand of a player"""
    def __init__(self, lst=[]):
        Deck.__init__(self, lst=lst)
        self.visible = False
        self.visible_to_player = True
