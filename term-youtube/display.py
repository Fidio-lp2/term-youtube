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

    def begin_drawing(self):
        """
        Begin Drawing.
        """
        curses.wrapper(self.main_loop)

    def main_loop(self, stdscr):
        """
        Main loop function.
        """
        pass
