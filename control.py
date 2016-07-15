#!/usr/bin/python

####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

import pygame
import random
import datetime
import logging

import log
pygame.init()
random.seed()

class map():

class tile():

class structural():

class dynamic():

class config():

class game_state():

class button():

class character():

class player():

class npc():

class gui(object):
	#the object that prints to the screen
    resolution = res_width, res_height = (1280, 720)
    cur_gui = None
    def set_res(self):
        self.display = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption('Hierarchy')
    def fill_color(self, screen, color, position):
        screen.fill(color)
        self.display.blit(screen, position)
    def write_text(self, size, message, color, location):
        font = pygame.font.Font(None, size)
        text = font.render(message, 1, color)
        textpos = text.get_rect()
        textpos.center = location
        self.display.blit(text, textpos)
    def set_subsurface(self, ss_dim):
        return self.display.subsurface(ss_dim)

    #def display_gui(self):
    #    self.

class intro_gui(gui):
    #set up intro surface
    def __init__(self):
        self.set_res()
        intro_screen_position = (0, 0)
        intro_screen = pygame.Surface(self.resolution)
        #fill black
        black = (0,0,0)
        self.fill_color(intro_screen, black, intro_screen_position)
        #draw title
        t_size = 108
        t_color = (255, 255, 255)
        t_message = 'Hierarchy'
        t_location = (self.display.get_width()/3,                        self.display.get_height()/4)
        self.write_text(t_size, t_message, t_color, t_location)
        # update cur_gui
        self.cur_gui = self
        #draw to display
        pygame.display.flip()


class map_gui(gui):

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
        pygame.display.flip()

    #Divide Map
    def get_map_ss(self):
        map_ss_dim = pygame.Rect(0, 0, 3*self.res_width/4, self.res_height)
        return self.set_subsurface(map_ss_dim)

    def get_active_map(self, game_map):
        # gen_map() // tbc
        active_map_dim = ((10000, 10000))
        active_map = pygame.Surface(active_map_dim)
        #fill some_color
        some_color = (245,165,44)
        pos = (0,0)
        self.fill_color(active_map, some_color, pos)
        return active_map

    #Get map segment from active map
    def get_map_seg(self, game_map, active_map, map_ss):
        map_seg_dim = pygame.Rect(0, 0, map_ss.get_width(), map_ss.get_height())
        loc = (0,0)
        return game_map.get_map_seg(active_map, map_seg_dim, loc)

    # get stats_panel and render to stats
    def get_stats_ss(self, map_ss):
        stats_ss_dim = pygame.Rect(map_ss.get_width(), 0, self.res_width/4, self.res_height)
        return self.set_subsurface(stats_ss_dim)

    def get_gui_buttons(self):
        # create dict of intro_gui buttons tuple (rect, type)
        return {'map_display': (pygame.Rect(0,0,100,200), 'gui')}



# add game_state
def event_loop(game_m, cur_g):
    #the object that manages events and time, using screen as an input
    # def player_input():
    # def player_output():
    # def objects_output():
        #monitors for key input and reports back to event loop
        #OUTPUT to EVENT QUEUE
    for event in pygame.event.get():
#           if type(intro_g.cur_gui) == intro_g:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                raise SystemExit
            elif event.key == pygame.K_SPACE:
                #go from intro screen to game screen
                map_display(game_m)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            try:
                buttons = cur_g.get_gui_buttons()
                button_key = does_click_button(buttons, mouse_pos)
            except AttributeError:
                # log print here
                print('gui %s has no method get_gui_buttons()' % type(cur_g))
                button_key = None
            if button_key:
                # all gui clicks here
                if buttons[button_key][1] == 'gui':
                    if button_key == 'map_display':
                        cur_g = map_display(game_m)
                    # other gui if's here

                # all other button types here
                return cur_g
    # if no event
    return cur_g


def does_click_button(buttons, mouse_pos):
    for b in buttons:
        if buttons[b][0].collidepoint(mouse_pos):
            return b
        else:
            return None

class game_map(object):
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


# class player_character(object):
# 	#storage for player attributes
# 	def map_input():
# 	def events_input():
# 	def objects_input():
# 	def map_output():
# 	def objects_output():
# 	def events_output():

# class game_state(object):
# 	#all objects on the map
# 	def events_input():
# 	def map_input():
# 	def player_input():
# 	def events_output():
# 	def map_output():
# 	def player_output():



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


# class map (object):

#     def __init__(self):
#         #initilise 2d array

# class map_tile(map):

#     self.map[x][y].id_num = 0
