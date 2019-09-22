"""
This module contains the card superclass of which creatures, sorcery, instants etc. are a subclass

todo: convert to superclass
todo: implement subclasses
"""


class Card:
    """"Represents the Card class"""
    def __init__(self, obj):
        self.name = obj['name']
        self.text = obj['text']
        self.type = obj['type']
        self.types = obj['types']
        self.tapped = True

    @property
    def info(self):
        """Logic to show all info of this card"""
        pass
