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
#import button
import game_map

pygame.init()


def event_loop(game_m, cur_g):
    #the object that manages events and time, using screen as an input
        #monitors for key input and reports back to event loop
        #OUTPUT to EVENT QUEUE
    for event in pygame.event.get():
#           if type(intro_g.cur_gui) == intro_g:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                raise SystemExit
            elif event.key == pygame.K_SPACE:
                #go from intro screen to game screen
                map_gui(game_m)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            #check if player has clicked a button
            try:
                ## return name of button clicked
                mouse_x = mouse_pos[0]
                mouse_y = mouse_pos[1]
                mouse_rect = pygame.Rect(mouse_x, mouse_y, 1, 1)
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
