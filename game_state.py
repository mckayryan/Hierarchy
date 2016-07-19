#!/usr/bin/python

####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

# libraries
import pygame
import logging
# hierarchy.py
import log
import gui
import button
import game_map
import config
import player
import npc
import tile


pygame.init()


class game_state(config):