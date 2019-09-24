"""
This module contains the Abstract Creature class

todo: add attributes
todo: flesh out functions
todo: add death function
todo: add destroy function
todo: make superclass; permanent (subclasses, land, creature etc.)
todo: make subclasses of creature? Flying?
todo: add counters
todo: add hexproof
todo: add keywords/evergreen keywords
"""

from abc import ABCMeta, abstractmethod


class AbstractCreature(metaclass=ABCMeta):
    """Abstract class to represent any creature type instance"""
    def __init__(self, name=''):
        self.toughness = 0
        self.name = name
        self.type = None
        self.tapped = True
        self.color = None
        self.cost = None
        self.power = 0
        self.trample = False
        self.deathtouch = False
        self.flying = False
        self.rarity = None
        self.summoning_sickness = True
        self.mana = 0

    @abstractmethod
    def info(self):
        """Print information about this game unit"""
        pass

    def untap(self):
        """Main logic to untap creature"""
        pass

    def attack(self):
        """Main logic to attack"""
        pass

    def block(self):
        """Main logic to block"""
        pass

    def heal(self):
        """Main logic to heal this unit"""
        pass

    def die(self):
        """Main logic to kill this unit"""
        pass

    def destroy(self):
        """Main logic to destroy this unit"""
        pass

    def exile(self):
        """Main logic to exile this unit"""
        pass
