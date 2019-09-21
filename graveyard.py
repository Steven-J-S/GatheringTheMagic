"""
This module contains the graveyard class

todo: add logic for pick() function; copy from deck Class
"""

from deck import Deck


class Graveyard(Deck):
    """Class to represent a graveyard"""
    def __init__(self, lst=[]):
        Deck.__init__(self, lst=lst)
        self.visible = True

    def pick(self):
        """Main logic to pick a card from the graveyard"""
        pass

    def search(self):
        """Main logic to search the graveyard for a card: input string"""
        pass
