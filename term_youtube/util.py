# -*- coding: utf-8 -*-
"""
Utility methods

"""
import shutil
import random
import os.path
from color import *


def dis_message(message: str, terminal_column) -> None:
    for i in range(int((terminal_column - len(message)) / 2)):
        print(' ', end='')
    print(green(message))

def threshold(wedge = ['>','<'], thre: str = '-'):
    terminal_size = shutil.get_terminal_size()
    print(yellow(wedge[0]) + ' ', end='')
    for i in range(terminal_size.columns - 5):
        print(yellow(thre), end='')
    print(' ' + yellow(wedge[1]))

def handler(func, *args):
    """
    Event handler.
    """
    func(*args)

def inves_app_path():
    """
    Investigate the absolute path of this app.
    """
    return (os.path.dirname(__file__))[:-13]

def welcome():
    print(" _                                              _         _")
    print("| |_ ___ _ __ _ __ ___        _   _  ___  _   _| |_ _   _| |__   ___")
    print("| __/ _ \\ '__| '_ ` _ \\ _____| | | |/ _ \\| | | | __| | | | '_ \\ / _ \\")
    print("| ||  __/ |  | | | | | |_____| |_| | (_) | |_| | |_| |_| | |_) |  __/")
    print(" \__\___|_|  |_| |_| |_|      \__, |\___/ \__,_|\__|\__,_|_.__/ \___|")
    print("                             |___/")
