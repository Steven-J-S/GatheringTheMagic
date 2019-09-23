"""
This module contains the Territory subclass, subclass of deck superclass
"""

from deck import Deck


class Territory(Deck):
    """Represents the territory class"""
    def __init__(self, lst=[]):
        Deck.__init__(self, lst=lst)
        self.visible = True

    @property
    def lands(self):
        """Logic to add lands from cards to lands; subdivision"""
        lands = list()
        for c in self.cards:
            if c.types[0] == 'Land':
                lands.append(c)
        return lands

    @property
    def creatures(self):
        """Logic to add creatures from cards to lands; subdivision"""
        creatures = list()
        for c in self.cards:
            if c.types[0] == 'Creature':
                creatures.append(c)
        return creatures

    @property
    def permanents(self):
        """Logic to show permanents on territory"""
        return self.cards

    @property
    def mana(self):
        """Logic to count all mana on territory"""
        mana = list()
        for l in self.lands:
            mana.append(l.manatype)
        return mana

    @property
    def available_mana(self):
        """Logic to list all untapped lands"""
        available_mana = list()
        for l in self.lands:
            if not l.tapped:
                available_mana.append(l.manatype)
        return available_mana

    def untap(self):
        """Logic to untap all cards in territory"""
        for c in self.cards:
            c.tapped = False
