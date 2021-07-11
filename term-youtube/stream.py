# -*- coding: utf-8 -*-
"""
Stream audio only with pafy and vlc from YouTube.

"""
import vlc
import pafy


class MusicStreamer:

    mediaList: vlc.MediaList
    player: vlc.MediaPlayer

    def __init__(self):
        self.mediaList= vlc.MediaList()
        self.player = vlc.MediaPlayer()
        self.player.set_media_list(self.mediaList)

    def play(self):
        self.player.play()

    def stop(self):
        self.player.stop()

    def next(self):
        self.player.next()

    def 

    def add_music(self, *urls):
        
