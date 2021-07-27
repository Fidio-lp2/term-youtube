# -*- coding:utf-8 -*-
"""
By displaying the Text-based user interface,
make being possible to control ``term-youtube`` interactive and intuitive.

"""
import curses


class DisplayYoutube:
    """
    Display and make being possible to control ``term-youtube``
    interactive and intuitive with curses.
    """

    def beginDrawing(self):
        """
        Begin Drawing.
        """
        curses.wrapper(mainLoop)

    def mainLoop(self, stdscr):
        """
        Main loop function.
        """
        print("hello")
