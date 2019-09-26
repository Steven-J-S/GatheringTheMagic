"""
This module contains the main code to play a game of Gathering the Magic

todo: menu, aantal players, welke deck (pick a deck option maken), start!
todo: list possible actions, attack, cast, play card
todo: begin; apply mandatory actions; untap, draw card, upkeep
todo: main phase; list actions
todo: combat; list actions
todo: end; apply ending logic
todo: while player.hit_points>0 toevoegen, anders verloren!
todo: player input toevoegen voor kaart keuze of mana keuze
todo: add timer for options (instants) that can be cast at any time
todo: split application and gameplay into seperate classes
todo: if player.health=<0 remove from players, if len(players)==1 end game
todo: add round and turn counter
todo: exception handling in inputs

Source for turn structure: https://mtg.gamepedia.com/Turn_structure
"""

import game.gameutils as gu
from itertools import cycle
from game.player import Player
from game.stack import Stack
from game.battlefield import Battlefield


class GatheringTheMagic:
    """Main class for the game"""
    def __init__(self):
        self.players = dict()
        self.stack = Stack()
        self.battlefield = Battlefield()

    @property
    def n_players(self):
        """Property to count players"""
        return len(self.players)

    def start_application(self):
        """Main logic to start application: menu, options etc."""
        """Run menu options then run game"""
        n = int(input('How many players?\n'))
        gu.clear_command_line()
        """Check number of players"""
        """Pass options to run_game()"""
        self.run_game(n)

    def run_game(self, n):
        """Main logic to run the game"""
        # Initialize players
        for i in range(n):
            name = str(input('Input name for player {}...\n'.format(str(i+1))))
            choice = input('Pick a deck for player {}...\n'.format(str(i+1)))
            deck_json = gu.load_deck(choice)
            deck = gu.build_deck(deck_json)
            value = Player(name, deck)
            key = 'Player_{}'.format(str(i+1))
            self.players[key] = value
        print('Players:')
        for k in self.players:
            print(self.players[k].name)
        # Loop game rounds as long as players are in the game
        self.game_round()

    def game_round(self):
        for k in cycle(self.players):
            self.game_turn(k)
            if self.n_players <= 1:
                self.end_game()

    def game_turn(self, k):
        gu.clear_command_line()
        gu.print_bold('It is {}\'s turn:'.format(self.players[k].name))
        self.begin_phase(k)
        self.main_phase(k)
        choice = ''
        while choice != 'y' and choice != 'n':
            choice = str(input('Enter combat phase? y/n\n'))
        if choice == 'y':
            self.combat_phase(self, k)
            self.main_phase(k)
        self.end_phase(k)
        # Check player.health
        for k in self.players:
            if self.players[k].health <= 0:
                del self.players[k]

    def begin_phase(self, k):
        self.players[k].territory.untap()
        self.players[k].take()

    def main_phase(self, k):
        gu.print_bold('Main phase')
        self.players[k].cast()
        self.players[k].use_ability()
        '''
        print('Main phase')
        choice = ''
        while choice != 'c' or 'p'
            choice = str(input('cast/pass'))
        if choice == 'c'
            card_idx = None
        while card_idx != in range(player.hand.count)
            card_idx = int(input('pick card idx'))
        player.cast(card_idx)
        else:
        pass
        '''

    def combat_phase(self, k):
        gu.print_bold('Combat phase')
        # Add logic to leave combat phase
        # Choose target
        # Choose attackers (cards)
        # Choose blockers (cards)
        # Resolve: tap/move to graveyard
        self.battlefield.resolve()
        pass

        '''
        print('Combat phase')
        print(players)
        target = input('Pick a target')
        attackers = input('Pick attackers')
        # pick attackers from list, confirm
        blockers = input('Pick blockers')
        # pick blockers from list, pick which attackers they will block, confirm
        # print setup
        # resolve
        '''

    def end_phase(self, k):
        # End turn
        pass

    def end_game(self):
        """Main logic to end the game: someone has won!"""
        pass


if __name__ == '__main__':
    game = GatheringTheMagic()
    game.start_application()
    print('Game ended!')

