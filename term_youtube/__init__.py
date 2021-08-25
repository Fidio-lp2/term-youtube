# -*- coding: utf-8 -*-

import sys
import readline
from .commandline import CommandLine
from .search import (
    fetch_video_url,
    fetch_video_names
)
from .stream import MusicStreamer
from .color import *
from .version import *

def welcome():
    print(" _   _  ___  _   _| |_ _   _| |__   ___  \n\
| | | |/ _ \| | | | __| | | | '_ \ / _ \\  \n\
| |_| | (_) | |_| | |_| |_| | |_) |  __/  \n\
 \__, |\___/ \__,_|\__|\__,_|_.__/ \___|  \n\
 |___/")

def search_video(input_val, video_num, player):
    names_list = fetch_video_names(input_val[7:], video_num)
    for i in range(len(names_list)):
        print(str(i) + " : " + names_list[i])

    while True:
        try:
            video_sub = input("Please input subscript. -> ")
            if video_sub == "cancel":
                print("Cancel!", end='')
                break
            if int(video_sub) < video_num and int(video_sub) > -1:
                break
            else:
                print("Input 0~" + str(video_num - 1) +
                        " value... One more please!", end='')
        except ValueError:
            print("Please input a number.")

    if video_sub != "cancel":
        url = fetch_video_url(names_list[int(video_sub)])
        player.add_songs(url)
        print(names_list[int(video_sub)] + " is added to playlist!", end='')


def _real_main():
    """
    Main script!!!
    """
    welcome()

    player = MusicStreamer()
    cmd = CommandLine(red('█')+bgred(white('▶︎'))+red('▉'))

    input_val: str
    print(cyan("Welcome to term-youtube!"))

    while True:
        input_val = cmd.commandline()

        # search settings
        if input_val[:6] == "search":
            while True:
                print()
                video_num_str = input("Please input the number that you want to search.\
                        \nDefault value is 10. -> ")
                try:
                    if video_num_str == '':
                        video_num_str = '10'
                    video_num = int(video_num_str)
                    break
                except ValueError:
                    print(red("[ERROR] An unexpected value has been detected."), end='')

            search_video(input_val, video_num, player)

        # stream settings
        elif input_val == "pause":
            player.pause()

        elif input_val == "next":
            player.next()

        elif input_val == "previous":
            player.previous()

        elif input_val[:4] == "play":
            if not input_val[5:] == '':
                player.add_songs(input_val[5:])
            player.play()

        elif input_val == "stop":
            player.stop()

        elif input_val[:3] == "add":
            player.add_songs(fetch_video_url(input_val[4:]))

        elif input_val == "exit":
            print()
            print("Thank you for using term-youtube!")
            break

        print()


def main():
    _real_main()
