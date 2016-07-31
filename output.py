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

from structure import button
from state import game_state
from tools import print_attr, wrap_text
from settings import config_obj, config

##
#
#
class gui(object):
    #the object that prints to the screen
    def set_res(self):
        res = config.get_res()
        self.display = pg.display.set_mode(res)
        pg.display.set_caption('Hierarchy')

    def set_subsurface(self, ss_dim):
        return self.display.subsurface(ss_dim)

    def fill_rect(self, location, color):
        ## this function can be hardware accellerated sometimes,
        # draw_rect() can't
        ## draws a colored rectangle on this gui at location
        ## pass location as Rect, color as string
        ## if location = None, whole surface will be filled
        color_rgb = config.get_color(color)
        ## fill(color, Rect)
        self.display.fill(color_rgb, location)

    def draw_rect(self, location, color, width):
        # draws a rectangle border on this gui at location,
        # with color and width
        # pass location as Rect, color as string, width as int
        # if width == 0, area will be filled
        color_rgb = config.get_color(color)

        # pg.draw.rect(surface, color, rect, width)
        pg.draw.rect(self.display, color_rgb, location, width)

    def fill_color(self, screen, color, position):
        screen.fill(config.get_color(color))
        self.display.blit(screen, position)

    def draw_gui_text(self):
        for loc in self.text:
            text, color, size = self.text[loc]
            self.draw_text(size, text, color, loc)

    def draw_text(self, size, message, color, location):
        font = pg.font.Font(None, size)
        text = font.render(message, 1, config.get_color(color))
        textpos = text.get_rect()
        textpos.topleft = location
        self.display.blit(text, textpos)
        return textpos

    def get_btns(self):
        return self.cur_btns

    def draw_gui_btns(self):
        for loc in self.cur_btns:
            dest, color, border, size, text = self.cur_btns[loc]
            if text:
                text_loc = (loc[0], loc[1])
                loc = self.draw_text(size, text, color, text_loc)

            self.draw_rect(loc, color, border)


##
#
#
class intro_gui(gui):

    def __init__(self):
        self.gui = 'intro_gui'
        self.set_res()

        # create dict of intro_gui buttons
        self.cur_btns = config.get_btns(self.gui)

        # entire intro screen
        self.main_surface = self.get_intro_ss()

        # draw text
        self.text = config.get_text(self.gui)
        self.draw_gui_text()

        self.draw_gui_btns()
        pg.display.flip()

    def get_intro_ss(self):
        ss_pos = (0, 0)
        intro_ss = pg.Surface(config.get_res())
        self.fill_color(intro_ss, 'black', ss_pos)
        return intro_ss



##
#
#
class map_gui(gui):

    def __init__(self, game_map):
        self.gui = 'map_gui'
        self.set_res()
        self.cur_btns = config.get_btns(self.gui)
        self.text = config.get_text(self.gui)

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

        # update display
        pg.display.flip()

    #Divide Map
    def get_map_ss(self):
        map_ss_x, map_ss_y = config.get_dim('map_ss')
        map_ss_dim = pg.Rect(0, 0, map_ss_x, map_ss_y)
        return self.set_subsurface(map_ss_dim)

    def get_active_map(self, game_map):
        # gen_map() // tbc
        active_map_dim = config.get_dim('active_map')
        active_map = pg.Surface(active_map_dim)
        #fill some_color
        pos = (0,0)
        self.fill_color(active_map, 'white', pos)
        return active_map

    #Get map segment from active map
    def get_map_seg(self, game_map, active_map, map_ss):
        map_seg_dim = pg.Rect(0, 0, map_ss.get_width(), map_ss.get_height())
        loc = (0,0)
        return game_map.get_map_seg(active_map, map_seg_dim, loc)

    # get stats_panel and render to stats
    def get_stats_ss(self, map_ss):
        stats_ss_x, stats_ss_y = config.get_dim('stats_ss')
        stats_ss_rect = pg.Rect(map_ss.get_width(), 0, stats_ss_x, stats_ss_y)
        return self.set_subsurface(stats_ss_rect)



##
#
#
class button(object):
    # tc
    pass
