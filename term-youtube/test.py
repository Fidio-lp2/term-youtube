import pafy
import vlc


player = vlc.MediaListPlayer()
urls = ["https://www.youtube.com/watch?v=vNuN8xH3X74", "https://www.youtube.com/watch?v=4IkLEmswL30"]
videos = [pafy.new(url) for url in urls]
bests = [video.getbestaudio() for video in videos]
playurls = [best.url for best in bests]
mediaList = vlc.MediaList(playurls)
player.set_media_list(mediaList)
player.set_playback_mode(vlc.PlaybackMode.loop)
player.play()

while True:
    pass
