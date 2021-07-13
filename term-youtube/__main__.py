# -*- coding:utf-8 -*-
"""
Main script...!

"""
from search import *
from stream import *


def main():
    player = MusicStreamer()

    player.add_song("https://www.youtube.com/watch?v=WeH2nuoQcYk")
    player.add_song("https://youtu.be/aCxOn3Pfljg")
    player.add_song("https://www.youtube.com/watch?v=5PTrZp5JJjk")

    player.play()

    key: str

    while True:
        key = input()

        if key == "pause":
            player.pause()

        elif key == "next":
            player.next()

        elif key == "brevious":
            player.previous()

        elif key == "start":
            player.play()

        elif key == "stop":
            player.stop()


if __name__ == "__main__":
    main()
