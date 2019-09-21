"""
This module contains the player class

Logic: Player contains...
Hand
Deck
Territory --> (remove) Battlefield has a player territory for each player
Graveyard

todo: add upkeep functionality
todo: cannot have more than 7 cards in hand
todo: if library is empty and player has to draw card, he loses
"""

from library import Library
from hand import Hand
from graveyard import Graveyard
from territory import Territory
from random import randint


class Player:
    """Class to represent a player"""
    def __init__(self, name, deck):
        self.name = name
        self.health = 20
        self.library = Library(deck)
        self.hand = Hand()
        self.take(amt=7, top=False)
        self.graveyard = Graveyard()
        self.territory = Territory()

    def take(self, amt=1, top=True):
        """Main logic to take a card from the top of the deck, if false take random"""
        if top:
            for i in range(amt):
                self.hand.cards.append(self.library.cards[0])
                del self.library.cards[0]
        else:
            for i in range(amt):
                idx = randint(0, self.library.count-1)
                self.hand.cards.append(self.library.cards[idx])
                del self.library.cards[idx]

    def redraw_hand(self):
        """Draw a new hand"""
        # Count redraws: 1 card less is drawn at every redraw
        pass

    def heal_self(self):
        """Main logic to heal player"""
        pass

    def receive_damage(self, value):
        """Main logic to damage player"""
        pass

    def cast(self):
        """Main logic to cast a card"""
        pass

    def use_ability(self):
        """Main logic to use any ability present in the territory"""
        pass

    def pick(self, type=None):
        """Main logic to pick a card of choice from the deck"""
        pass

    def put(self, card=None):
        """Main logic to put a card in the deck"""
        pass

    def search(self, name=''):
        """Main logic to search the deck for a card: input string"""
        pass

    def look(self):
        """Main logic to look at top card"""
        pass

    def exile(self):
        """Main logic to exile a card (choice: hand, territory or graveyard)"""
        pass
