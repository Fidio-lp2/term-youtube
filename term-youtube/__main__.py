# -*- coding:utf-8 -*-
"""
Main script...!

"""
import sys
from .search import (
        fetch_video_data,
        fetch_video_names,
        fetch_video_url,
        fetch_video_name
)
from .stream import *
    

def main():
    """
    Main script!!!
    """
    # sys.stderr = open("out.log", "w")

    player = MusicStreamer()

    player.play()

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

        elif key == "start":
            player.play()

        elif key == "stop":
            player.stop()

        elif key[:3] == "add":
            player.add_songs(key[4:])

        elif key == "exit":
            break

    # sys.stderr.close()


if __name__ == "__main__":
    main()
