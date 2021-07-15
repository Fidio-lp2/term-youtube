# -*- coding:utf-8 -*-
"""
Main script...!

"""
import sys
from search import *
from stream import *


def main():
    """
    Main script!!!
    """
    # sys.stderr = open("out.log", "w")

    player = MusicStreamer()

    player.add_song("https://www.youtube.com/watch?v=tE8nzUQ_q_Y")
    player.add_song("https://www.youtube.com/watch?v=ZM7brmvzumE")
    player.add_song("https://www.youtube.com/watch?v=5PTrZp5JJjk")
    player.add_song("https://www.youtube.com/watch?v=bWo982dwTLI")
    player.add_song("https://www.youtube.com/watch?v=n0sWvKrEYT8")

    player.play()

    key: str

    while True:
        key = input()

        if key == "pause":
            player.pause()

        elif key == "next":
            player.next()

        elif key == "previous":
            player.previous()

        elif key == "start":
            player.play()

        elif key == "stop":
            player.stop()

        elif key == "exit":
            break

    # sys.stderr.close()


if __name__ == "__main__":
    main()
