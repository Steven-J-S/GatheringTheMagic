"""
This module contains the artifact class
"""

from game.card import Card


class Artifact(Card):
    """Class to represent artifacts"""
    def __init__(self, obj):
        Card.__init__(self, obj)

    def info(self):
        """Show info of card"""
        pass
