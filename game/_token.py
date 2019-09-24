"""
This module contains the token class

todo: make token a subclass of creature? (or of permanent superclass)
todo: make token a superclass of creature token or other type
"""


class Token:
    """Class to represent a token"""
    def __init__(self):
        self.type = None
        self.hit_points = 0
        self.attack_power = 0
        self.tapped = True
