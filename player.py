"""
This module contains the player class

Logic: Player contains...
Hand
Deck
Territory
Graveyard

todo: add upkeep functionality
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
        if self.hand.count >= 7:
            print('(Already 7 cards in hand!)')
            pass
        elif top:
            for i in range(amt):
                self.hand.cards.append(self.library.cards[0])
                del self.library.cards[0]
        else:
            for i in range(amt):
                idx = randint(0, self.library.count-1)
                self.hand.cards.append(self.library.cards[idx])
                del self.library.cards[idx]

    def cast(self):
        """Main logic to cast a card"""
        # Pick a card from hand: input
        print('Cast a card from your hand:')
        for c in range(self.hand.count):
            print('[' + str(c) + '] '+str(self.hand.cards[c].name))
        card_idx = None
        while card_idx not in range(self.hand.count):
            card_idx = int(input('Card: '))

        # Play this card to territory if creature or land, else: pass (for now)
        if self.hand.cards[card_idx].types[0] == 'Land':
            self._cast_land(card_idx)
        elif self.hand.cards[card_idx].types[0] == 'Creature':
            self._cast_creature(card_idx)
        else:
            pass

    def _cast_land(self, card_idx):
        """Main logic to cast land card"""
        self.territory.cards.append(self.hand.cards[card_idx])
        del self.hand.cards[card_idx]

    def _cast_creature(self, card_idx):
        """Main logic to cast creature card"""
        # Check mana cost of creature card
        # Check mana in territory
        # Cast card or print error

        manaCost = self.hand.cards[card_idx].manaCost
        # input('Creature costs: ' + str(manaCost) + ', tap lands:')

        self.territory.cards.append(self.hand.cards[card_idx])
        del self.hand.cards[card_idx]

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
