"""
This module contains the planeswalker class
"""

from game.card import Card


class PlanesWalker(Card):
    """Class to represent planeswalker"""
    def __int__(self, obj):
        Card.__init__(self, obj)
        self.hit_points = 0
        self.abilities = list()

    def use_ability(self):
        """Main logic to use one of the abilities"""
        pass

