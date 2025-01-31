"""
This module contains the card superclass of which creatures, sorcery, instants etc. are a subclass

todo: convert to superclass
todo: implement subclasses
todo: fix abstract method instantiation error
"""

from abc import ABCMeta, abstractmethod


class Card(metaclass=ABCMeta):
    """"Represents the Card class"""
    def __init__(self, obj):
        self.name = obj['name']
        # self.text = obj['text']
        self.type = obj['type'].replace('—', '-')
        self.types = obj['types']
        self.subtypes = obj['subtypes']
        self.tapped = False

    @property
    # @abstractmethod <------------------- raises error!
    def info(self):
        """Logic to show all info of this card"""
        pass
