#!/usr/bin/python

####    Hierarchy
##      Creators: Adam Stiles and Ryan McKay
##      July 2016
##      Made in Python

## Heirarchy is a game of survival that urges the player to discover what it means to be Human.

import datetime
import logging

from setup import config

class logger(config):

    def __init__():
        LOG_FILENAME = str(datetime.date.today()) + ".hierarchy.log"
        LOG_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        LOG_DATEFMT = '%I:%M:%S %p'
        ## Set logging level
        logging_config = dict(
            version = 1,
            formatters = {
                'f': {'format': LOG_FORMAT,
                      'datefmt': LOG_DATEFMT}
                },
            handlers = {
                'h': {'class': 'logging.FileHandler',
                      'formatter': 'f',
                      'level': config.log_level["info"],
                      'filename': LOG_FILENAME,
                      'mode': 'w'}
                },
            root = {
                'handlers': ['h'],
                'level': config.log_levels["info"],
                },
        )
        dictConfig(logging_config)
        print (logging.getLogger())
