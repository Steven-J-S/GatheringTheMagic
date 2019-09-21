"""
This module contains the land class

todo: add logic to untap land
todo: add logic to choose which land to tap
"""


class Land:
    """Class to represent land instances"""
    def __init__(self):
        self.type = None
        self.mana = 1
        self.tapped = True

    def info(self):
        """Show the info of instance"""
        pass

    def untap(self):
        """Main logic to untap land"""
        pass
