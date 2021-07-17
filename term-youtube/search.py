# -*- coding: utf-8 -*-
"""
Fetch information of movie in youtube.

"""
import json
from typing import Final
from googleapiclient.discovery import build
from util import inves_app_path

# youtube api token is read from other file ignored .gitignore
tokenpath: str = inves_app_path() + "/.token.json"
with open(tokenpath, "r") as tokenFile:
    YOUTUBE_API_TOKEN: Final[str] = (json.load(tokenFile))["youtubeApiToken"]
URL_HEADER: Final[str] = "https://www.youtube.com/watch?v="


def fetch_video_data(search_name, video_num):
    """
    Fetch data of video in youtube

    This method is take information of videos in youtube with google
    youtube api. Other methods in this module, search module use this method.
    So if you delete this method, they will not be usable.

    Parameters
    ----------
    search_name : str
        Video name you want information of video.
    video_num : int
        Nunmber of video information you want.

    Returns
    -------
    response : resource
        Data of video in like json file format.
    """
    query: str = search_name
    video_cnt: int = video_num + 5
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_TOKEN)
    response = youtube.search().list(
        q=query,
        part="id,snippet",
        maxResults=video_cnt
    ).execute()

    i: int = 0
    while i < len(response["items"]):
        try:
            response["items"][i]["id"]["videoId"]
        except KeyError:
            response["items"].pop(i)
            continue
        i += 1

    while True:
        if len(response["items"]) > video_num:
            response["items"].pop(len(response["items"]) - 1)
        elif len(response["items"]) <= video_num:
            break

    return response


def fetch_video_name(search_name):
    """
    Fetch video title on youtube come on the top after searching.

    Parameters
    ----------
    search_name : str
        Video name you want.

    Returns
    -------
    name : str
        Video title you want.
    """
    response = fetch_video_data(search_name, 1)

    name = response["items"][0]["snippet"]["title"]

    return name


def fetch_video_names(search_name, video_num):
    """
    Fetch a list of video title.

    Parameters
    ----------
    search_name : str
        Video name you want.
    video_num : int
        Number of the video title you want.

    Returns
    -------
    names : list[str]
        List of video title.
    """
    response = fetch_video_data(search_name, video_num)

    names = [item["snippet"]["title"] for item in response["items"]]

    return names


def fetch_video_url(search_name):
    """
    Fetch a url of video in youtube come on the top after searching.

    Parameters
    ----------
    search_name : str
        Video name you want url.

    Returns
    -------
    URL_HEADER : str
        Video url.
    """
    datas = fetch_video_data(search_name, 1)

    return URL_HEADER + datas["items"][0]["id"]["videoId"]
