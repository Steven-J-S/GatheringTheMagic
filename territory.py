"""
This module contains the Territory subclass, subclass of deck superclass
"""

from deck import Deck


class Territory(Deck):
    """Represents the territory class"""
    def __init__(self, lst=[]):
        Deck.__init__(self, lst=lst)
        self.visible = True

    def untap(self):
        """Logic to untap all cards in territory"""
        for c in self.cards:
            self.cards[c].tapped = False

