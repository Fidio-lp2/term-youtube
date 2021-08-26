# -*- coding: utf-8 -*-

import sys
import shutil
import readline
from .commandline import CommandLine
from .search import (
    fetch_video_url,
    fetch_video_names
)
from .stream import MusicStreamer
from .util import *
from .color import *
from .version import *


terminal_size = shutil.get_terminal_size()

def welcome():
    print(red('█')+bgred(white('▶︎'))+red('▉'), end='')
    print(cyan(" ------------------------------------"))
    print(cyan("| Welcome to term-youtube " + get_version() + " !       |"))
    print(cyan("| Type 'help', can know basic operation." + '|'))
    print(cyan(" ---------------------------------------"))


def search_video(input_val, video_num, player):
    
    threshold()

    names_list = fetch_video_names(input_val[7:], video_num)
    for i in range(len(names_list)):
        print(magenta(str(i)) + green(" : " + names_list[i]))

    threshold()

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
            print(red("[ERROR] Please input a number."))

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
    cmd = CommandLine(blue('>'))

    input_val: str

    while True:
        terminal_size = shutil.get_terminal_size()
        input_val = cmd.commandline()
        print()

        #              #
        # Main Process #
        #              #

        # Search the song and add to the current current list
        if input_val[:6] == "search":
            while True:
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

            print()

        # Pause the song that is streaming now.
        elif input_val == "pause":
            player.pause()
            dis_message("-*- Streaming is paused! -*-",
                    terminal_size.columns)

        # Go to the next song
        elif input_val == "next":
            player.next()
            dis_message("-*- Skip to next song! -*-",
                    terminal_size.columns)

        # Go back to the previous song
        elif input_val == "previous":
            player.previous()
            dis_message("-*- Go back to the previous song! -*-",
                    terminal_size.columns)

        # Stream the current play list from the begining
        elif input_val[:4] == "play":
            if not input_val[5:] == '':
                player.add_songs(fetch_video_url(input_val[5:]))
            player.play()
            dis_message("-*- Streaming is play! -*-",
                    terminal_size.columns)

        # Stop the current song list
        elif input_val == "stop":
            player.stop()
            dis_message("-*- Streaming is stopped! -*-",
                    terminal_size.columns)

        # Streaming mode settings
        elif input_val == "default":
            player.set_mode(0)
            dis_message("-*- Switch default mode! -*-",
                    terminal_size.columns)
        elif input_val == "loop":
            player.set_mode(1)
            dis_message("-*- Switch loop mode! -*-",
                    terminal_size.columns)
        elif input_val == "repeat":
            player.set_mode(2)
            dis_message("-*- Switch repeat mode! -*-",
                    terminal_size.columns)

        # Add song to the current song list
        elif input_val[:3] == "add":
            player.add_songs(fetch_video_url(input_val[4:]))
            dis_message("-*- Added song to the current playlist! -*-",
                    terminal_size.columns)

        elif input_val[:6] == "remove":
            try:
                remove_subs = [int(s.strip()) for s in input_val[7:].split(',')]
                player.remove_songs(remove_subs)
                dis_message("-*- Remove songs! -*-",
                        terminal_size.columns)

            except ValueError:
                print(red("[ERROR] Subscript is unexpected."))

        # Display the current song list
        elif input_val == "list":
            video_list = player.inves_current_list()
            threshold(['#','#'], '=')
            idx: int = 0
            for video in video_list:
                if idx == player.inves_song_index():
                    print(blue('♪'), end='')
                else:
                    print(magenta(str(idx)), end='')
                print(green(" : " + video.title))
                idx += 1
            if len(video_list) == 0:
                for i in range(int((terminal_size.columns -15) / 2)):
                    print(' ', end='')
                print(green("No songs added!"))
            threshold(['#','#'], '=')

        elif input_val[:4] == "data":
            video_list = player.inves_current_list()
            video_subs = []
            try:
                if input_val[5:].strip() == "all":
                    video_subs = [i for i in range(len(video_list))]
                elif input_val[5:] != '':
                    video_subs = [int(i.strip()) for i in input_val[5:].split(',')]
                elif input_val[5:] == '':
                    video_subs = [player.inves_song_index()]

                threshold(['=','='])

                for sub in video_subs:
                    if sub == player.inves_song_index():
                        print(blue('♪'), end='')
                    else:
                        print(magenta(str(sub)), end='')
                    print(' '+bgwhite(black("Title", bold=True)) +' '+ video_list[sub].title +\
                            ' ['+white(video_list[sub].duration, line=True)+']')
                    print(bgblack(white("Author", bold=True)) + ' ' + video_list[sub].author)
                    print()
                    print(green("Description" + "\n-----------\n") + video_list[sub].description)
                    print(green("-----------"))
                    print()
                    print(bgwhite(black("⤴︎ :" + str(video_list[sub].likes))) \
                            + bgblack(white(" ⤵︎ :" + str(video_list[sub].dislikes))))
                    print(str(video_list[sub].viewcount) + " views " + video_list[sub].published)

                    threshold(['=','='])

            except ValueError:
                print(red("[ERROR] Subscript is unexpected."))


        # Make the play list
        elif input_val[:4] == "make":
            list_name: str = input_val[5:].strip()
            if list_name == '':
                print(red("[ERROR] Please input list name."))

        # Clear the screen
        elif input_val == "clear":
            sys.stdout.write("\033[2J\033[H" + blue("[term-youtube]\n"))
            sys.stdout.flush()

        # Exit from this application
        elif input_val == "exit":
            print()
            print(cyan("-*- Thank you for using term-youtube! -*- "))
            break


def main():
    _real_main()
