"""
This module contains the sorcery class
"""

from game.card import Card


class Sorcery(Card):
    """Class to represent a sorcery type card"""
    def __init__(self, obj):
        Card.__init__(self, obj)
        # self.flavorText = obj['flavorText']
        self.manaCost = obj['manaCost']
        self.convertedManaCost = obj['convertedManaCost']
        self.power = None
        self.toughness = None
        self.summoningSickness = True

    def info(self):
        """Show info of card"""
        pass
