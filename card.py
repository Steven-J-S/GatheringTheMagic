"""
This module contains the card superclass of which creatures, sorcery, instants etc. are a subclass
"""


class Card:
    """"Represents the Card class"""
    def __init__(self):
        self.type = None
        self.tapped = True
