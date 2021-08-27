# term-youtube

If you use this application, you can listen to YouTube music on **command line‼️*

gazou

## Dependency

You should use after `python-3.9.0` version.

And, set the environment variable "GOOGLE_YOUTUBE_API_TOKEN" to your "YouTube Data API". 

## Requirement
module:
1. `python-vlc`
2. `python-pafy`
3. `googleapiclient`

## Usage

You can enter the term-youtube's commandline by typing `term-youtube`.

### basic commands

`play [title]`

Please input song name or its url to [title]. It can also be used to play playlists described below. [title] is not neccesary.

`add [title]`

Please input song name or its url to [title]. Add the most popular song searched by title to the current playlist.

`pause`

Pause the streaming song. This command is toggle.

`stop`

Stop the current streaming. When type `play`, streaming play from the begining.

`next`

Skip to the next song.

`previous`

Go back one to the previous song.

`list`

Show you songs of the current playlist.

`status`

Show you the current mode, the current playlist, the playing song... etc.

`data [song sub]`

Show you the song data. [song sub] can be inputed the value confirmed by `list` command.
If you don't specified, display the playing song data. If you specified `all` to [song sub], display the all song data.

`clear`

Clear the screen.

`exit`

Quit this app.

### mode setting commands

`default`

Set the playback mode to the default.

`loop`

Set the playback mode to the loop. In this mode, streaming is loop in the current playlist.

`repeat`

Set the playback mode to the repeat. In this mode, streaming is repeat the current song.


### playlist commands

`playlist`

Show you the list of the existing playlist. Default playlist name is `None`.

`open [playlist name]`

Open [playlist name]. `None` playlist is temporarily evacuated.

`back`

Go back to `None` playlist.

'save [name]'

Save the current playlist as [name]. [name] is never used `None`. And, `None` playlist cannot be saved. And, this command cannnot be overwritten.

`delete [name]`

Delete the [name] playlist. If [name] playlist is locked, this operation will be undone.

`update [name]`
 
 Overwrite the [name] playlist with the current playlist. If you don't specified [name], [name] is the current playlist name. If [name] playlist is locked, this operation will be undone.

 `rename [name]`

 Rename the current playlist to [name]. If [name] playlist is locked, this operation will be undone.

`lock [name]`

Disables changing of the [name] playlist.

`unlock [name]`

Enable changing of the [name] playlist.

## Install

To install with git,

```
git glone "https://github.com/Fidio-lp2/term-youtube"
```

and, create path to `bin/` directory in this repository.

## Author

