#!/usr/bin/python

####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

# libraries
import pygame as pg
import logging
# hierarchy.py
from settings import config_obj, config
from structure import game_map
from state import game_state
from control import event_loop
from output import gui, intro_gui


##
#
#
def main():
    #global config
    #logger = config.get_logger('info')
    #logger.info('In main')
    pg.init()
    # initialise modules
    game_m = game_map()
    cur_g = intro_gui()
    while True:
        # game_map, game_state, cur_gui
        cur_g = event_loop(game_m, cur_g)


if __name__ == "__main__" and __package__ is None:
    # import sys
    # from os import path
    # cmd_subfolder =  path.realpath( path.abspath( path.join( path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
    # if cmd_subfolder not in sys.path:
    #     sys.path.insert(0, cmd_subfolder)
    main()
    sys.exit()
