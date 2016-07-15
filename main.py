#!/usr/bin/python

####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

# libraries
import pygame
# hierarchy.py
import gui
import game_map
import game_state

pygame.init()

def main():
    #initialise modules
    intro_g = intro_gui()
    game_m = game_map()
    cur_g = intro_g
    while True:
        # game_map, game_state, cur_gui
        cur_g = event_loop(game_m, cur_g)


if __name__ == "__main__":
    main()
    sys.exit()
