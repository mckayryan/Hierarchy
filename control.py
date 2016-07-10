#!/usr/bin/python

####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

import pygame
import random
pygame.init()
random.seed()


class GUI(object):

    def __init__(self):
        #set window screen res - pixels
        self.resolution = res_width, res_height = (1280, 720)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption('Hierarchy')
        #Divide Map
        self.map_screen_dim = map_positionx, map_positiony, map_width, map_height  = (0, 0, 3*res_width/4, res_height)
        self.map_screen_position = pygame.Rect(self.map_screen_dim)
        self.map_sub_screen = self.screen.subsurface(self.map_screen_position)
        # Divide Stats screen
        self.stats_screen_dim = stats_positionx, stats_positiony, stats_width, stats_height = (map_width, 0, res_width/4, res_height)
        self.stats_screen_position = pygame.Rect(self.stats_screen_dim)
        self.stats_sub_screen = self.screen.subsurface(self.stats_screen_position)

        #Initiate map surface - pixels
        self.whole_map_dim = ((10000, 10000))
        self.whole_map = pygame.Surface(self.whole_map_dim)
        #fill black, RGB
        black = (0,0,0)
        self.whole_map.fill(black)

        #Mount a section of the map surfacen the map screen
        self.map_segment_dim = segment_posx, segment_posy, segment_width, segment_height = (0, 0, map_width, map_height)
        self.map_segment = pygame.Rect(self.map_segment_dim)
        self.map_sub_screen.blit(self.whole_map.subsurface(self.map_segment), (0,0))

        #Draw to display
        pygame.display.flip()



def main():
    screen = GUI()



if __name__ == "__main__":
    main()
