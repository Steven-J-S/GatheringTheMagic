"""
This module contains the land class

todo: add logic to choose which land to tap
"""

from game.card import Card


class Land(Card):
    """Class to represent land instances"""
    def __init__(self, obj):
        Card.__init__(self, obj)
        # self.flavorText = None

    @property
    def manatype(self):
        if self.subtypes[0] == 'Plains':
            manatype = 'W'
        elif self.subtypes[0] == 'Island':
            manatype = 'U'
        elif self.subtypes[0] == 'Swamp':
            manatype = 'B'
        elif self.subtypes[0] == 'Mountain':
            manatype = 'R'
        elif self.subtypes[0] == 'Forest':
            manatype = 'G'
        elif self.subtypes[0] == 'Wastes':
            manatype = None
        return manatype
