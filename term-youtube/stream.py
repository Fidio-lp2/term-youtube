# -*- coding: utf-8 -*-
"""
Stream audio only with pafy and vlc from YouTube.

"""
from typing import Callable
import vlc
import pafy


class MusicStreamer:
    """
    The Wrapper of pafy and python-vlc with audio only.

    Attributes
    ----------
    media_list : vlc.MediaList
        Python-vlc's class that store song.
    player : vlc.MediaListPlayer
        Python-vlc's class that stream songs mainly.
    """

    media_list: vlc.MediaList
    player: vlc.MediaListPlayer

    def __init__(self):
        """
        Constructor.
        """
        self.media_list = vlc.MediaList()
        self.player = vlc.MediaListPlayer()
        self.player.set_media_list(self.media_list)

    # wrapper methods
    def play(self):
        """
        Play streaming.
        """
        self.player.play()

    def stop(self):
        """
        Stop streaming.
        """
        self.player.stop()

    def next(self):
        """
        Go to the next song.
        """
        self.player.next()

    def previous(self):
        """
        Go back to the previous song.
        """
        self.player.previous()

    def pause(self):
        """
        Pause streaming. (toggle)
        """
        self.player.pause()

    def add_song(self, *urls):
        """
        Add song.
        """
        videos = [pafy.new(url) for url in urls]
        bests = [video.getbestaudio() for video in videos]
        playurls = [best.url for best in bests]
        for mrl in playurls:
            self.media_list.add_media(mrl)

    def stream(self):
        key: str
        
        while True:
            key = input()
