#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Christoph Pranzl"
__copyright__ = "Copyright 2020, Christoph Pranzl"
__credits__ = ["Christoph Pranzl"]
__license__ = "GNU GPLv3"
__version__ = "0.0.1"
__maintainer__ = "Christoph Pranzl"
__email__ = "christoph.pranzl@pranzl.net"
__status__ = "prototype"

"""
SYNOPSIS
    ancientsymbols [-h,--help] [-v,--verbose] [--version]
DESCRIPTION

EXAMPLES

"""
import sys, os, traceback, argparse
import time
import random
from logzero import logger

GREEN = ['1','2','3','Terror','Peril','Lore']
YELLOW = ['1','2','3','4','Peril','Lore']
RED = ['2','3','Peril','Lore','Joker']

dicepool = [GREEN,GREEN,GREEN,GREEN,GREEN,GREEN]

diceresults = []

def roll(dicepool):
    diceresults.clear()
    for dice in dicepool:
        result = random.sample(dice,1)
        diceresults.append(result)

def main(args):
    """ Main entry point of the app """
    roll(dicepool)

    for result in diceresults:
        logger.info(result)

    dicepool.append(RED)
    roll(dicepool)

    for result in diceresults:
        logger.info(result)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser =  argparse.ArgumentParser()
    parser.add_argument("-v", \
                        "--verbose", \
                        action="store_true", \
                        default=False, \
                        help="increase verbose output")
    parser.add_argument('--version', \
                        action='version', \
                        version='%(prog)s ' + __version__)
    args = parser.parse_args()
    main(args)
