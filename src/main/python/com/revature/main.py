#!/usr/bin/env python3
import logging
from controller import controller
from ioDAO import ioDAO

'''
This is your main script, this should call several other scripts within your packages.
'''

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('resources/transactions.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def main():
    # ioDAO.setLogger()
    cont = controller.Controller()
    cont.start()


if __name__ == '__main__':
    main()
