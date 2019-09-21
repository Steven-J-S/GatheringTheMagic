"""
This module contains the main code to play a game of Gathering the Magic

todo: menu, aantal players, welke deck (pick a deck option maken), start!
todo: list possible actions, attack, cast, play card
todo: game opdelen in beurten (game -> round -> turn -> phases -> steps)
todo: phase opdelen: begin -> main phase -> combat -> main phase -> end
todo: begin; apply mandatory actions; untap, draw card, upkeep
todo: main phase; list actions
todo: combat; list actions
todo: end; apply ending logic
todo: while player.hit_points>0 toevoegen, anders verloren!
todo: player input toevoegen voor kaart keuze of mana keuze
todo: add timer for options (instants) that can be cast at any time
todo: make play_game a class
todo: split application and gameplay into seperate classes
todo: if player.health=<0 remove from players, if len(players)==1 end game
todo: add round and turn counter
todo: exception handling in inputs

Source for turn structure: https://mtg.gamepedia.com/Turn_structure
"""

import json
import gameutils
from itertools import cycle
from player import Player
from stack import Stack
from battlefield import Battlefield


def start_application():
    """Main logic to start application: menu, options etc."""
    """Run menu options then run game"""
    n_players = int(input('How many players?\n'))
    """Check number of players"""
    """Pass options to run_game()"""
    run_game(n_players)


def run_game(n_players):
    """Main logic to run the game"""

    # Initialize players
    players = {}
    for i in range(n_players):
        name = str(input('Input name for player {}...\n'.format(str(i+1))))
        choice = input('Pick a deck for player {}...\n'.format(str(i+1)))
        with open('Decks/'+choice+'.json', 'r', encoding='utf-8-sig') as f:
            deck = json.load(f)
        value = Player(name, deck['mainBoard'])
        key = 'Player_{}'.format(str(i+1))
        players[key] = value
    print('Players:\n')
    for k in players:
        print(players[k].name)

    # Initialize stack
    stack = Stack()

    # Initialize battlefield
    battlefield = Battlefield()

    # Loop game rounds as long as players are in the game
    while len(players) > 1:
        game_round(players, battlefield)
    else:
        end_game()


def game_round(players, battlefield):
    for k in cycle(players):
        print('It is {}\'s turn:'.format(players[k].name))
        game_turn(players, k, battlefield)


def game_turn(players, k, battlefield):
    begin_phase(players[k])
    main_phase(players[k])
    choice = ''
    while choice != 'y' and choice != 'n':
        str(input('Enter combat phase? y/n\n'))
    if choice == 'y':
        combat_phase(players[k], battlefield)
        main_phase(players[k]) # (if combat phase is played)
    end_phase(players[k])
    # Check player.health
    for k in players:
        if players[k].health <= 0:
            del players[k]


def begin_phase(player):
    player.territory.untap()
    player.library.take()


def main_phase(player):
    player.cast()
    player.use_ability()


def combat_phase(player, battlefield):
    # Add logic to leave combat phase
    # Choose target
    # Choose attackers (cards)
    # Choose blockers (cards)
    # Resolve: tap/move to graveyard
    battlefield.resolve()
    pass


def end_phase(player):
    # End turn
    pass


def end_game():
    """Main logic to end the game: someone has won!"""
    pass


if __name__ == '__main__':
    start_application()
    print('Game ended!')

