#!/usr/bin/python

####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

import pygame as pg
import datetime
import logging
from logging.config import dictConfig


class config(object):
    ## These values can be modified
    log_levels = {  "debug": logging.DEBUG,
                    "info": logging.INFO,
                    "warning": logging.WARNING }

    def __init__(self):
        pass
