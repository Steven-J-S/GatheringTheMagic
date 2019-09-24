"""
This module contains the Deck superclass of which library, graveyard, exile and hand are a subclass

Note: Deck is in principe een (abstract) container voor kaarten; a collection of objects
"""


class Deck:
    """Class to represent deck type; container for cards"""
    def __init__(self, lst=[]):
        self.cards = lst.copy()  # Use copy because it will be mutated in the game code

    @property
    def count(self):
        """Dynamic properties"""
        return len(self.cards)
