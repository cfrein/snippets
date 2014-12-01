"""
Who:    Claus Frein
Why:    Collection of small python-snippets
When:   20120131: Created
"""

import sys
import logging

def simple_logger(loglevel="ERROR", name="", format="%(message)s"):
    """simple logging to console
    """
    if not hasattr(logging, loglevel.upper()):
        print("unknown loglevel {}".format(loglevel))
        sys.exit(1)
    else:
        numericlevel = getattr(logging, loglevel.upper())
        logging.basicConfig(level=numericlevel, format=format)
        logger = logging.getLogger(name)
        return logger

def add_logfile(logger, name, format="%(asctime)s %(levelname)s:%(message)s"):
    formatter = logging.Formatter(format)
    fh = logging.FileHandler(name)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
