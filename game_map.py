#!/usr/bin/python

####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

# libraries
import pygame
# hierarchy.py
import button
import config

pygame.init()

class game_map(config):
    #storage of updatable *4 pixel object map
    #also includes structural map at *64 pixel
    def events_input():
        pass
    # def player_input():
    # def objects_input():
    def events_output():
        pass
    # def player_output():
    # def objects_output():
    def get_map_seg(self, active_map, dim, loc):
        # tb moved back to map_gui and just gen map seg
        return active_map.subsurface(dim)

    def generate_map(game_map):
        #fills an empty game map with the starting game state
        pass
