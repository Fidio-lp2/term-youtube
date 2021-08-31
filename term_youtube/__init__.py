# -*- coding: utf-8 -*-

import sys
import json
import shutil
import datetime
# MAGIC SPELL
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

PLAYLIST_PATH = inves_app_path() + "/playlist.json"

def welcome():
    print(red('█')+bgred(white('▶︎'))+red('▉'), end='')
    print(cyan(" ------------------------------------"))
    print(cyan("| Welcome to term-youtube " + get_version() + " !       |"))
    print(cyan("| Type 'help', can know basic operation." + '|'))
    print(cyan(" ---------------------------------------"))

def get_playlist():
    with open(PLAYLIST_PATH) as file:
        return json.load(file)

def save_playlist(jsonfile):
    with open(PLAYLIST_PATH, 'w') as file:
        json.dump(jsonfile, file)

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
        if input_val[:7].strip() == "search":
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
            dis_message("-*- Streaming is paused! -*-")

        # Go to the next song
        elif input_val == "next":
            player.next()
            dis_message("-*- Skip to next song! -*-")

        # Go back to the previous song
        elif input_val == "previous":
            player.previous()
            dis_message("-*- Go back to the previous song! -*-")

        # Stream the current play list from the begining
        elif input_val[:5].strip() == "play":
            if not input_val[6:] == '':
                if input_val[4:8].strip() == "at":
                    try:
                        player.play_at_index(int(input_val[8:]))
                        player.play()
                        dis_message("-*- Streaming is play! -*-")
                    except ValueError:
                        print(red("[ERROR] An unexpected value."))
                    except IndexError:
                        print(red("[ERROR] Not existing the index."))
                else:
                    player.add_songs(fetch_video_url(input_val[5:]))
                    player.play()
                    dis_message("-*- Streaming is play! -*-")
            else:
                player.play()
                dis_message("-*- Streaming is play! -*-")


        # Stop the current song list
        elif input_val == "stop":
            player.stop()
            dis_message("-*- Streaming is stopped! -*-")

        # Streaming mode settings
        elif input_val == "default":
            player.set_mode(0)
            dis_message("-*- Switch default mode! -*-")
        elif input_val == "loop":
            player.set_mode(1)
            dis_message("-*- Switch loop mode! -*-")
        elif input_val == "repeat":
            player.set_mode(2)
            dis_message("-*- Switch repeat mode! -*-")

        # Add song to the current song list
        elif input_val[:4].strip() == "add":
            player.add_songs(fetch_video_url(input_val[4:]))
            dis_message("-*- Added song to the current playlist! -*-")

        # Remove song of the current playlist
        elif input_val[:7].strip() == "remove":
            try:
                remove_subs = [int(s.strip()) for s in input_val[7:].split(',')]
                player.remove_songs(remove_subs)
                dis_message("-*- Remove songs! -*-")

            except ValueError:
                print(red("[ERROR] Subscript is unexpected."))

        # Display the current playlist
        elif input_val[:5].strip() == "list":
            playlist_name = player.get_playlist_name() if input_val[5:].strip() == '' \
                    else input_val[5:].strip()
            playlist = get_playlist()
            if playlist_name in playlist.keys() or playlist_name == "None":
                print(yellow("# "+playlist_name+" #"))
                threshold(['#','#'], '=')
                idx: int = 0
                if playlist_name == "None":
                    video_list = [songs.title for songs in player.inves_list(playlist_name)]
                else:
                    video_list = playlist[playlist_name]['songs']
                for video_name in video_list:
                    if idx == player.inves_song_index() and player.is_playing():
                        print(blue('♪'), end='')
                    else:
                        print(magenta(str(idx)), end='')
                    print(green(" : " + str(video_name)))
                    idx += 1
                if len(video_list) == 0:
                    for i in range(int((terminal_size.columns -15) / 2)):
                        print(' ', end='')
                    print(green("No songs added!"))
                threshold(['#','#'], '=')

            else:
                print(red("[ERROR] No matched name playlist."))

        # Show the data of songs of the current playlist
        elif input_val[:5].strip() == "data":
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
                    if sub == -1:
                        raise IndexError
                    if sub == player.inves_song_index() and player.is_playing():
                        print(blue('♪'), end='')
                    else:
                        print(magenta(str(sub)), end='')
                    print(' '+bgwhite(black("Title", bold=True)) +' '+ video_list[sub].title +\
                            ' ['+white(video_list[sub].duration, line=True)+']')
                    print(bgblack(white("Author", bold=True)) + ' ' + video_list[sub].author)
                    print()
                    print(green("Description" + "\n-----------\n") + video_list[sub].description)
                    print(green("-----------"))
                    print(bgwhite(black("⤴︎ :" + str(video_list[sub].likes))) \
                            + bgblack(white(" ⤵︎ :" + str(video_list[sub].dislikes))))
                    print(str(video_list[sub].viewcount) + " views " + video_list[sub].published)

                    threshold(['=','='])

            except ValueError:
                print(red("[ERROR] Subscript is unexpected."))

            except IndexError:
                dis_message("No song data!")
                threshold(['=','='])

        elif input_val == "status":
            threshold(['<','>'], '~')
            mode = {0:"default", 1:"loop", 2:"repeat"}
            try:
                if player.is_playing():
                    song_data = (player.inves_current_list())[player.inves_song_index()]
                    m, s = divmod(int(player.inves_song_pos() * song_data.length) , 60)
                    h, m = divmod(m, 60)
                    dura_per = int(100 * player.inves_song_pos())
                    print(bgblack(blue("♪ Now playing...\n", bold=True)) + ' ' + song_data.title)
                    print('[' + white(f'{h:02d}:{m:02d}:{s:02d}', line=True) + '/' +\
                            white(str(song_data.duration), line=True) + ']' + ' ', end='')
                    print('(' + str(dura_per) + '%)')
            except IndexError:
                pass
            print(" playlist name : " + player.get_playlist_name())
            print(" mode : " + mode[player.get_mode()])
            threshold(['<','>'], '~')



        #                    #
        # PlayList Operation #
        #                    #

        # Show the all playlist list
        elif input_val == "playlist":
            threshold(['#','#'], '-')
            playlist = get_playlist()
            exist_playlist: bool = False
            for title in playlist.keys():
                exist_playlist = True
                print(' ' + magenta(title) + ' - ' + green(playlist[title]['uptime']) +\
                        ' ', end='')
                if playlist[title]['lock'] == 1:
                    print(yellow("(lock) "), end='')
                else:
                    pass
                if player.get_playlist_name() == title:
                    print(blue("(open)"))
                else:
                    print()
            if not exist_playlist:
                dis_message("-*- No playlists! -*-")
            threshold(['#','#'], '-')

        # Make the play list
        elif input_val[:5].strip() == "save":
            list_name: str = input_val[5:].strip()
            playlist = get_playlist()
            video_list = player.inves_current_list()
            song_list = [song.title for song in video_list]
            data = datetime.datetime.now()
            if not list_name == "None":
                if not list_name in playlist.keys():
                    playlist[list_name] = {
                        "songs" : song_list,
                        "uptime" : str(data)[:19],
                        "lock" : 0
                    }
                    save_playlist(playlist)
                    player.save_playlist()
                    dis_message("-*- Saved "+ list_name + "! -*-")
                else:
                    print(red("[ERROR] The playlist of name is existing."))
            else:
                print(red("[ERROR] Please use a name other than None."))

        elif input_val[:7].strip() == "delete":
            list_name: str = input_val[7:].strip()
            playlist = get_playlist()
            if list_name in playlist.keys():
                if playlist[list_name]['lock'] == 0:
                    res = input("Do you really want to delete " + list_name + "? [y/n]\n-> ")
                    if res == 'y':
                        playlist.pop(list_name)
                        save_playlist(playlist)
                        player.delete_playlist(list_name)
                        dis_message("-*- Deleted " + list_name + "! -*-")
                    else:
                        pass
                else:
                    dis_message("-*- " + list_name + " is locked! -*-")
            else:
                print(red("[ERROR] No matched name playlist."))

        elif input_val == "back":
            player.back_playlist()

        elif input_val[:5].strip() == "open":
            list_name: str = input_val[5:]
            playlist = get_playlist()
            if list_name in playlist.keys():
                song_urls = [fetch_video_url(name) for name in playlist[list_name]['songs']]
                player.open_playlist(list_name, song_urls)
                dis_message("Opend " + list_name + "!")
            else:
                print(red("[ERROR] No matched name playlist."))

        elif input_val[:7].strip() == "update":
            list_name: str = input_val[7:].strip()
            list_name = player.get_playlist_name() if list_name == '' else list_name
            playlist = get_playlist()
            video_list = player.inves_current_list()
            song_list = [song.title for song in video_list]
            if list_name in playlist.keys():
                if playlist[list_name]['lock'] == 0:
                    res = input("Do you really want to update " + list_name + "? [y/n]\n-> ")
                    if res == 'y':
                        playlist[list_name]['songs'] = song_list
                        save_playlist(playlist)
                        player.update_playlist()
                        dis_message("-*- Updated "+ list_name + "! -*-")
                else:
                    dis_message("-*- " + list_name + " is locked! -*-")
            else:
                print(red("[ERROR] No matched name playlist."))

        elif input_val[:7].strip() == "rename":
            playlist = {}
            list_name: str = input_val[7:].strip()
            current_name = player.get_playlist_name()
            playlist = get_playlist()
            if current_name in playlist.keys():
                if playlist[current_name]['lock'] == 0:
                    res = input("Do you really want to rename " + list_name + "? [y/n]\n-> ")
                    if res == 'y':
                        data = playlist.pop(current_name)
                        playlist[list_name] = data
                        save_playlist(playlist)
                        player.rename_playlist(list_name)
                        dis_message("-*- Renamed " + current_name +" to "+ list_name + "! -*-")
                else:
                    dis_message("-*- " + current_name + " is locked! -*-")
            else:
                print(red("[ERROR] No matched name playlist."))

        elif input_val[:5].strip() == "lock":
            playlist = {}
            list_name: str = input_val[5:].strip()
            playlist = get_playlist()
            if list_name in playlist.keys():
                playlist[list_name]['lock'] = 1
                save_playlist(playlist)
                dis_message("-*- Locked " + list_name + "! -*-")
            else:
                print(red("[ERROR] No matched name playlist."))

        elif input_val[:7].strip() == "unlock":
            playlist = {}
            list_name: str = input_val[7:].strip()
            playlist = get_playlist()
            if list_name in playlist.keys():
                playlist[list_name]['lock'] = 0
                save_playlist(playlist)
                dis_message("-*- Unlocked " + list_name + "! -*-")
            else:
                print(red("[ERROR] No matched name playlist."))

        #        #
        # Others #
        #        #

        # Clear the screen
        elif input_val == "clear":
            sys.stdout.write("\033[2J\033[H" + blue("-*- term-youtube -*-\n"))
            sys.stdout.flush()

        # Exit from this application
        elif input_val == "exit":
            print(cyan("-*- Thank you for using term-youtube! -*- "))
            break


def main():
    _real_main()
