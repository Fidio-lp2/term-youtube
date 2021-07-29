#!/Users/fidio/.pyenv/shims/python
# -*- coding:utf-8 -*-
"""
Main script...!

"""
import daemon
from search import (
        fetch_video_names,
        fetch_video_url
)
from stream import MusicStreamer


player = MusicStreamer()

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


CALLBACKS = {
    "search": search_video,
    "play": player.play,
    "stop": player.stop,
    "pause": player.pause,
    "next": player.next,
    "previous": player.previous,
    "add": player.add_songs
}


def main():
    """
    Main script!!!
    """
    key: str

    while True:
        key = input()

        # search settings

        if key[:9] == "ty search":
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

        elif key == "ty pause":
            player.pause()

        elif key == "ty next":
            player.next()

        elif key == "ty previous":
            player.previous()

        elif key == "ty play":
            player.play()

        elif key == "ty stop":
            player.stop()

        elif key[:3] == "ty add":
            player.add_songs(key[4:])

        elif key == "ty exit":
            break


if __name__ == "__main__":
    main()
