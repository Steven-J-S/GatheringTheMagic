"""
This module contains the land class

todo: add logic to choose which land to tap
"""

from card import Card


class Land(Card):
    """Class to represent land instances"""
    def __init__(self, obj):
        Card.__init__(self, obj)
        # self.flavorText = None
        self.manaCost = None
        self.convertedManaCost = None
        self.power = None
        self.toughness = None
        self.summoningSickness = None
