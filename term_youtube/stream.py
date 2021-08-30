# -*- coding: utf-8 -*-
"""
Stream audio only with pafy and vlc from YouTube.

"""
import vlc
import pafy
import pafy.backend_youtube_dl


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

    media_list: dict[str, vlc.MediaList] = {}
    player: vlc.MediaListPlayer
    video_datas: dict[str, list[pafy.backend_youtube_dl.YtdlPafy]] = {}
    play_mode: int
    playlist_name: str

    def __init__(self):
        """
        Constructor.
        """
        self.player = vlc.MediaListPlayer()
        self.playlist_name = "None"
        self.play_mode = 0
        self.media_list[self.playlist_name] = vlc.MediaList()
        self.player.set_media_list(self.media_list[self.playlist_name])
        self.video_datas[self.playlist_name] = []

    # wrapper methods
    def play(self):
        """
        Play streaming.
        """
        self.player.play()

    def play_at_index(self, index: int):
        self.player.play_item_at_index(index)

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

    def get_playlist_name(self):
        """
        Return the current playlist name.
        """
        return self.playlist_name

    def add_songs(self, *urls):
        """
        Add songs.

        Parameters
        ----------
        *urls : list[str]
            List of the video urls in youtube.
        """
        videos = [pafy.new(url) for url in urls]
        self.video_datas[self.playlist_name] += videos
        bests = [video.getbestaudio() for video in videos]
        playurls = [best.url for best in bests]
        for mrl in playurls:
            self.media_list[self.playlist_name].add_media(mrl)

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
            if sub > -1 and sub <= len(self.video_datas[self.playlist_name]) - dicre_idx:
                self.video_datas[self.playlist_name].pop(sub)
                self.media_list[self.playlist_name].remove_index(sub)
                dicre_idx += 1

    def is_playing(self):
        """
        Return whether it is playing.
        """
        return self.player.is_playing()

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
        index = self.media_list[self.playlist_name].index_of_item(media_instance)

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

        return self.video_datas[self.playlist_name]

    def inves_list(self, playlist_name):
        return self.video_datas[playlist_name]

    def open_playlist(self, list_name, song_urls=[]):
        self.playlist_name = list_name
        self.media_list[self.playlist_name] = vlc.MediaList()
        self.player.set_media_list(self.media_list[self.playlist_name])
        self.video_datas[self.playlist_name] = []
        for url in song_urls:
            self.add_songs(url)

        return 0

    def save_playlist(self):
        pass

    def delete_playlist(self, playlist_name):
        if playlist_name in self.video_datas.keys():
            self.media_list.pop(playlist_name)
            self.video_datas.pop(playlist_name)
            self.player.set_media_list(self.media_list["None"])
            if playlist_name == self.playlist_name:
                self.playlist_name = "None"

    def update_playlist(self):
        pass

    def rename_playlist(self, playlist_name):
        media = self.media_list.pop(self.playlist_name)
        data = self.video_datas.pop(self.playlist_name)
        self.playlist_name = playlist_name
        self.media_list[self.playlist_name] = media
        self.video_datas[self.playlist_name] = data

    def back_playlist(self):
        self.playlist_name = "None"
        self.player.set_media_list(self.media_list[self.playlist_name])

class PlayList():
    name: str
    

class __MovieData():
    pass
