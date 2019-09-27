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
            '|\033[1m' + self.name + ' '*(20 - len(self.name)) + '\033[0m|',
            '|' + self.manaCost + ' '*(20 - len(self.manaCost)) + '|',
            '|\033[1m' + self.type + ' '*(20 - len(self.type)) + '\033[0m|',
            '|' + self.power + '/' + self.toughness + ' '*(19 - len(self.power) - len(self.toughness)) + '|',
            '|Tapped: ' + str(self.tapped) + ' '*(12 - len(str(self.tapped))) + '|',
            '|SumSick: ' + str(self.summoningSickness) + ' '*(11 - len(str(self.summoningSickness))) + '|',
            '|_' + '_' * 18 + '_|'
        ]
        return info
