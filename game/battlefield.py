"""
This module contains the battlefield class

Note: lijkt op de deck class maar bij de deck class is alles verborgen (behalve in het geval)
      van een hand. Bij battlefield is alles open.

todo: add battlefield sections (subclasses?): territories (friendly), battleground (disputed)
            (should battleground contain the stack?)
todo: make battlefield contain all others (stack, territories, etc.)
"""

from game.deck import Deck


class Battlefield:
    """Class to represent the battlefield"""
    def __init__(self):
        attackers = Deck()
        blockers = Deck()

    def resolve(self):
        """Resolve combat phase"""
        pass
