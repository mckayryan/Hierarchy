#!/usr/bin/python

####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

import datetime
import logging

## Set our logging levels
LOG_LEVELS = {
              "debug": logging.DEBUG,
              "info": logging.INFO,
              "warning": logging.WARNING
              }

## Set logging level
# if config.log_level in LOG_LEVELS:
#     log_level = log_level = LOG_LEVELS["info"]
# else:
log_level = LOG_LEVELS["info"]
print (log_level)
# create log file
logging.basicConfig(
            filename= str(datetime.date.today()) + ".hierarchy.log",
            format='%(asctime)s:%(levelname)s:%(message)s',
            datefmt='%I:%M:%S %p',
            filemode='w',
            level=log_level
            )
