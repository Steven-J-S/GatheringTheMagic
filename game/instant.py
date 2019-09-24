"""
This module contains the instant class
"""

from game.card import Card


class Instant(Card):
    """Class to represent an instant card"""
    def __init__(self, obj):
        Card.__init__(self, obj)
        # self.flavorText = obj['flavorText']
        self.manaCost = obj['manaCost']
        self.convertedManaCost = obj['convertedManaCost']
        self.power = None
        self.toughness = None
        self.summoningSickness = True