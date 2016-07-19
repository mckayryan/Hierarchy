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
from tools import logger
from output import gui
#import button
from structure import game_map
from state import game_state
from output import gui, intro_gui, map_gui


def event_loop(game_m, cur_g):
    #the object that manages events and time, using screen as an input
        #monitors for key input and reports back to event loop
        #OUTPUT to EVENT QUEUE
    for event in pg.event.get():
#           if type(intro_g.cur_gui) == intro_g:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                raise SystemExit
            elif event.key == pg.K_SPACE:
                #go from intro screen to game screen
                map_gui(game_m)
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_pos = pg.mouse.get_pos()

            #check if player has clicked a button
            try:
                ## return name of button clicked
                mouse_x = mouse_pos[0]
                mouse_y = mouse_pos[1]
                mouse_rect = pg.Rect(mouse_x, mouse_y, 1, 1)
                # check mouse location against dict of buttons
                mouse_btn = mouse_rect.collidedict(cur_g.cur_btns)

                # if no button has been clicked
                if mouse_btn == None:
                    button_key = None
                else:
                    # name of the button clicked (top in dict)
                    button_key = mouse_btn[1]
            except AttributeError:
                # log print here
                #print('gui %s has no method get_gui_buttons()' % type(cur_g))
                button_key = None

            #if a button has been clicked
            if button_key:
                # all gui clicks here
                if button_key == 'map_gui':
                    #let the current gui be the map_gui
                    cur_g = map_gui(game_m)
                # other gui if here
                # all other button types here
                return cur_g
    # if no event
    return cur_g
