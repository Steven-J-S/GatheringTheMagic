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
        # Make these subclasses
        if obj['types'][0] == 'Land':
            # self.flavorText = None
            self.manaCost = None
            self.convertedManaCost = None
            self.power = None
            self.toughness = None
            self.summoningSickness = None
        elif obj['types'][0] == 'Creature':
            # self.flavorText = obj['flavorText']
            self.manaCost = obj['manaCost']
            self.convertedManaCost = obj['convertedManaCost']
            self.power = obj['power']
            self.toughness = obj['toughness']
            self.summoningSickness = True
        elif obj['types'][0] == 'Instant' or obj['types'][0] == 'Sorcery':
            # self.flavorText = obj['flavorText']
            self.manaCost = obj['manaCost']
            self.convertedManaCost = obj['convertedManaCost']
            self.power = None
            self.toughness = None
            self.summoningSickness = True

    def info(self):
        """Logic to show all info of this card"""
        pass
