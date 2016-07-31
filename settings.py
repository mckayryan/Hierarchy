#!/usr/bin/python

####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

import pygame as pg
import os
import datetime
import logging
from collections import defaultdict
from tools import create_logger, print_attr


class config_obj(object):
    def __init__(self):
        ##
        # All initial values go here
        #
        self.res = res_x, res_y = (1280, 720)
        self.dis_rect = pg.Rect(0, 0, res_x, res_y)
        # formatt: 'gui_title': {(rect_loc, text, color, border, size, text)}
        self.btn =   {
                'intro_gui':    {
                            (res_x/2, res_y/1.5, 200, 100) : ('map_gui', 'white', 1, 48, 'PLAY GAME')
                            },
                'map_gui':  {
                        (0,0,100,200) : ('intro_gui', 'white', 1, None, False)
                        }
                }

        self.dim =   {
                'full_map': (12800, 12800),
                'active_map': (15/8*res_x, 5/2*res_y),
                'map_ss': (3/4*res_x, res_y),
                'stats_ss': (res_x/4, res_y),
                'tile': (64, 64)
                }

        ## format
        #'gui_title': {(center_loc, text, color, size)}
        self.text = {
                'intro_gui':    {
                    (res_x/2,res_y/3) : ('Hierarchy','white', 108),
                    }

            }
        ## perhaps should be a dict with 'key': value
        #                   =>   'game_object': color
        self.color_ref = {
                    'black': (0,0,0),
                    'white': (255, 255, 255)
                    }

         #map_obj_key = {'@': pg.Rect()}

        # tile

        ## These values can be modified
        log_level = {
                    "debug": logging.DEBUG,
                    "info": logging.INFO,
                    "warning": logging.WARNING
                    }
        logger_detail = {
                        'filename': os.path.join('logs/',  str(datetime.date.today()) + '.hierarchy.log'),
                        'basic': '%(asctime)-4s %(name)s %(levelname)-4s/ %(funcName)s "%(message)s"',
                        'verbose': '%(asctime)-4s %(name)s %(levelname)-4s/                                        %(funcName)s "%(message)s"',
                        'date': '%I:%M:%S%p'
                        }
        # Init logger
        create_logger(log_level, logger_detail)



        # { 'origin_gui': { btn_loc: (dest_gui, color, width)}}

        #print (type(btn))
        #print_attr(BTN)

    def get_res(self):
            return self.res

    def get_logger(self, log_level):
        try:
            return logging.getLogger(log_level)
        except ValueError:
            return logging.getLogger('info')

    def get_text(self, text_key):
        try:
            return self.text[text_key]
        except KeyError:
            logger = self.get_logger('info')
            logger.info('', exc_info=True)

    def get_dim(self, dim_key):
        try:
            return self.dim[dim_key]
        except KeyError:
            logger = self.get_logger('info')
            logger.info('', exc_info=True)

    def get_btns(self, gui):
        try:
            return self.btn[gui]
        except KeyError:
            logger = self.get_logger('info')
            logger.info('', exc_info=True)

    def get_color(self, color):
        try:
            return self.color_ref[color]
        except KeyError:
            logger = self.get_logger('info')
            logger.info('', exc_info=True)

config = config_obj()
