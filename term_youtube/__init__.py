# -*- coding: utf-8 -*-

import sys
import daemon
from .search import *
from .stream import *


def search_video(key):
    names_list = fetch_video_names(key[7:], 10)
    for i in range(len(names_list)):
        print(str(i) + " : " + names_list[i])

        while True:
            video_sub = input()
            if video_sub == "cancel":
                print("Cancel!")
                break
            if int(video_sub) < 10 and int(video_sub) > -1:
                break
            else:
                print("Input 0~9 value... One more please!")

        if video_sub != "cancel":
            url = fetch_video_url(names_list[int(video_sub)])
            player.add_songs(url)
            print(names_list[int(video_sub)] + " is added to playlist!")

def play_song():
    pass

def stop_song():
    pass

def pause_song():
    pass

def next_song():
    pass

def next_song():
    pass

def previous_song():
    pass

def add_songs():
    pass

CALLBACKS = {
    "search": search_video,
    "play": play_song,
    "stop": stop_song,
    "pause": pause_song,
    "next": next_song,
    "previous": previous_song,
    "add": add_songs
}


def _real_main():
    """
    Main script!!!
    """
    player = MusicStreamer

    key: str

    while True:
        key = input()

        # search settings

        if key[:6] == "search":
            names_list = fetch_video_names(key[7:], 10)
            for i in range(len(names_list)):
                print(str(i) + " : " + names_list[i])

            while True:
                video_sub = input()
                if video_sub == "cancel":
                    print("Cancel!")
                    break
                elif int(video_sub) < 10 and int(video_sub) > -1:
                    break
                else:
                    print("Input 0~9 value... One more please!")

            if video_sub != "cancel":
                url = fetch_video_url(names_list[int(video_sub)])
                player.add_songs(url)
                print(names_list[int(video_sub)] + "is added to playlist!")

        # stream settings

        elif key == "pause":
            player.pause()

        elif key == "next":
            player.next()

        elif key == "previous":
            player.previous()

        elif key == "play":
            player.play()

        elif key == "stop":
            player.stop()

        elif key[:3] == "add":
            player.add_songs(key[4:])

        elif key == "exit":
 
def main():
    _real_main()
