"""
This module contains the Creature class
"""

from game.card import Card


class Creature(Card):
    """Class to represent a creature card"""
    def __init__(self, obj):
        Card.__init__(self, obj)
        # self.flavorText = obj['flavorText']
        self.manaCost = obj['manaCost']
        self.convertedManaCost = obj['convertedManaCost']
        self.power = obj['power']
        self.toughness = obj['toughness']
        self.summoningSickness = True

    def info(self):
        """Show info of card"""
        pass
