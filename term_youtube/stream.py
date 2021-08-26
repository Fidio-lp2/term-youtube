# -*- coding: utf-8 -*-
"""
Stream audio only with pafy and vlc from YouTube.

"""
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
    my_videos = []
    play_mode: int

    def __init__(self):
        """
        Constructor.
        """
        self.media_list = vlc.MediaList()
        self.player = vlc.MediaListPlayer()
        self.player.set_media_list(self.media_list)
        self.play_mode = 0

    # wrapper methods
    def play(self):
        """
        Play streaming.
        """
        self.player.play()

    def stop(self):
        """
        Stop streaming.

        If you used this method, streaming stop and
        reset at the beginning of the song.
        If you want to pause, you can use the pause() method.
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
        Pause streaming. This method is toggle.
        """
        self.player.pause()

    def set_mode(self, mode_sub: int):
        """
        Set the playing mode.
        """
        mode = [
            vlc.PlaybackMode.default,
            vlc.PlaybackMode.loop,
            vlc.PlaybackMode.repeat
        ]
        self.player.set_playback_mode(mode[mode_sub])
        self.play_mode = mode_sub

    def get_mode(self):
        """
        Return the current playing mode.
        """
        return self.play_mode

    def add_songs(self, *urls):
        """
        Add songs.

        Parameters
        ----------
        *urls : list[str]
            List of the video urls in youtube.
        """
        videos = [pafy.new(url) for url in urls]
        self.my_videos += videos
        bests = [video.getbestaudio() for video in videos]
        playurls = [best.url for best in bests]
        for mrl in playurls:
            self.media_list.add_media(mrl)

    def remove_songs(self, movie_subs):
        """
        Delete songs.

        Parameters
        ----------
        movie_subs : list[int]
            List of the subscript of videos that you want to delete in current playlist.
        """
        movie_subs = sorted(movie_subs)
        dicre_idx: int = 0
        for sub in movie_subs:
            sub -= dicre_idx
            if sub > -1 and sub <= len(self.my_videos) - dicre_idx:
                self.my_videos.pop(sub)
                self.media_list.remove_index(sub)
                dicre_idx += 1

    def inves_song_index(self) -> int:
        """
        Investigate the index of the song that is streaming.

        Returns
        -------
        index : int
            The index of the song that is streaming.
        """
        media = self.player.get_media_player()
        media_instance = media.get_media()
        index = self.media_list.index_of_item(media_instance)

        return index

    def inves_song_pos(self) -> float:
        """
        Investigate the position of the song that is streaming.

        Returns
        -------
        pos : float
            The position of the song that is streaming.
        """
        media = self.player.get_media_player()
        pos = media.get_position()

        return pos

    def inves_current_list(self):

        return self.my_videos

class PlayList():
    name: str
    

class __MovieData():
    pass
