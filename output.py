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

from setup import config
from structure import button
from state import game_state

##
#
#
class gui(config):
    #the object that prints to the screen
    resolution = res_width, res_height = (1280, 720)
    cur_gui = None
    color_ref = {'black': (0,0,0), 'white': (255, 255, 255)}
    def set_res(self):
        self.display = pg.display.set_mode(self.resolution)
        pg.display.set_caption('Hierarchy')

    def set_subsurface(self, ss_dim):
        return self.display.subsurface(ss_dim)

    def write_text(self, size, message, color, location):
        font = pg.font.Font(None, size)
        text = font.render(message, 1, color)
        textpos = text.get_rect()
        textpos.center = location
        self.display.blit(text, textpos)

    def fill_rect(self, location, color):
        ## this function can be hardware accellerated sometimes,
        # draw_rect() can't
        ## draws a colored rectangle on this gui at location
        ## pass location as Rect, color as string
        ## if location = None, whole surface will be filled
        color_rgb = self.get_color(color)
        ## fill(color, Rect)
        self.display.fill(color_rgb, location)

    def draw_rect(self, location, color, width):
        # draws a rectangle border on this gui at location,
        # with color and width
        # pass location as Rect, color as string, width as int
        # if width == 0, area will be filled
        color_rgb = self.get_color(color)
        # pg.draw.rect(surface, color, rect, width)
        pg.draw.rect(self.display, color_rgb, location, width)

    def fill_color(self, screen, color, position):
        screen.fill(color)
        self.display.blit(screen, position)

    def get_color(self, color):
        #input color as a string and return RBG code
        return self.color_ref[color]


##
#
#
class intro_gui(gui):
    #set up intro surface
    # create dict of intro_gui buttons

    cur_btns = { (200,520,200,100) : 'map_gui'}
    def __init__(self):
        self.set_res()
        intro_screen_position = (0, 0)
        intro_screen = pg.Surface(self.resolution)
        #fill black
        self.fill_rect(None, 'black')
        #draw title
        t_size = 108
        t_color = (255, 255, 255)
        t_message = 'Hierarchy'
        t_location = (self.display.get_width()/3, self.display.get_height()/4)
        self.write_text(t_size, t_message, t_color, t_location)

        # draw button
        # this is horrible, but there will be button objects later
        btn_location = (200,520,200,100)
        color = 'white'
        width = 5
        self.draw_rect(btn_location, color, width)
        # def set_button(): rect = () -> draw_button(rect) (in class button)
        # text in button
        t_size = 48
        t_color = self.color_ref['white']
        t_message = 'PLAY'
        t_location = (300, 570)
        self.write_text(t_size, t_message, t_color, t_location)
        # update cur_gui
        self.cur_gui = self
        #draw to display
        pg.display.flip()



##
#
#
class map_gui(gui):
    cur_btns = {}

    def __init__(self, game_map):
        self.set_res()
        # gui subsurface map block
        map_ss = self.get_map_ss()
        # active portion of game_map
        active_map = self.get_active_map(game_map)
        # portion of active_map rendered to map_ss
        map_seg = self.get_map_seg(game_map, active_map, map_ss)
        # surface (stats_panel) to render on stats_ss
        stats_ss = self.get_stats_ss(map_ss)
        pos = (0,0)
        map_ss.blit(map_seg, pos)
        self.cur_gui = self
        # update display
        pg.display.flip()

    #Divide Map
    def get_map_ss(self):
        map_ss_dim = pg.Rect(0, 0, 3*self.res_width/4, self.res_height)
        return self.set_subsurface(map_ss_dim)

    def get_active_map(self, game_map):
        # gen_map() // tbc
        active_map_dim = ((10000, 10000))
        active_map = pg.Surface(active_map_dim)
        #fill some_color
        some_color = (245,165,44)
        pos = (0,0)
        self.fill_color(active_map, some_color, pos)
        return active_map

    #Get map segment from active map
    def get_map_seg(self, game_map, active_map, map_ss):
        map_seg_dim = pg.Rect(0, 0, map_ss.get_width(), map_ss.get_height())
        loc = (0,0)
        return game_map.get_map_seg(active_map, map_seg_dim, loc)

    # get stats_panel and render to stats
    def get_stats_ss(self, map_ss):
        stats_ss_dim = pg.Rect(map_ss.get_width(), 0, self.res_width/4, self.res_height)
        return self.set_subsurface(stats_ss_dim)

    def get_gui_buttons(self):
        # create dict of intro_gui buttons tuple (rect, type)
        return {'map_gui': (pg.Rect(0,0,100,200), 'gui')}


##
#
#
class button(config):
    # tc
    pass
