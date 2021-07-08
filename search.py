# -*- coding: utf-8 -*-
""" module docstring


"""

import json
from typing import Final
from googleapiclient.discovery import build

# youtube api token is read from other file ignored .gitignore
with open(".token.json", "r") as tokenFile:
    KEY: Final[str] = (json.load(tokenFile))["youtubeApiToken"]
HEADER: Final[str] = "https://www.youtube.com/watch?v="

def get_video_data(search_name, video_num):
    """
    Get data of video in youtube



    Parameters
    ----------
    search_name : str
        video name you want information of video
    video_num : int
        nunmber of video information you want

    Returns
    -------
    response : resource
        data of video in like json file format
    """

    query: str = search_name
    video_cnt: int = video_num + 5
    youtube: resource = build("youtube","v3",developerKey=KEY)
    response = youtube.search().list(
                q=query,
                part="id,snippet",
                maxResults = video_cnt
    ).execute()

    i: int = 0
    while i < len(response["items"]):
        try:
            response["items"][i]["id"]["videoId"]
        except KeyError:
            response["items"].pop(i)
            continue
        i+=1

    while True:
        if len(response["items"]) > video_num:
            response["items"].pop(len(response["items"])-1)
        elif len(response["items"]) <= video_num:
            break

    return response

def get_video_name(search_name):
    """
    get video name 
    """

    response = get_video_data(search_name, 1)
 
    name = response["items"][0]["snippet"]["title"]

    return name

def get_video_names(search_name, video_num):
    response = get_video_data(search_name, video_num)
    
    names = [item["snippet"]["title"] for item in response["items"]]

    return names

# return video url
def get_video_url(search_name):
    datas = get_video_data(search_name, 1)
    
    return HEADER + datas["items"][0]["id"]["videoId"]
