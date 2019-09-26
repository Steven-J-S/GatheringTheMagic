"""
This module contains the Creature class
"""

from game.card import Card


class Creature(Card):
    """Class to represent a creature card"""
    def __init__(self, obj):
        Card.__init__(self, obj)
        # self.flavorText = obj['flavorText']
        self.manaCost = obj['manaCost']
        self.convertedManaCost = obj['convertedManaCost']
        self.power = obj['power']
        self.toughness = obj['toughness']
        self.summoningSickness = True

    def info(self):
        """Show info of card"""
        info = [
            ' _' + '_' * 18 + '_ ',
            '|' + self.name + ' ' * (18 - len(self.name)) + '|',
            '|' + self.manaCost + ' ' * (18 - len(self.manaCost)) + '|',
            '|' + self.type + ' ' * (18 - len(self.type)) + '|',
            '|' + self.power + '/' + self.toughness + ' ' * (17 - len(self.power) - len(self.toughness)) + '|',
            '| Tapped: ' + str(self.tapped) + ' ' * (9 - len(str(self.tapped))) + '|',
            '| SumSick: ' + self.type + ' ' * (8 - len(self.type)) + '|',
            '|_' + '_' * 18 + '_|'
        ]
        return info
