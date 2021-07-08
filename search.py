from googleapiclient.discovery import build
from typing import Final
import json

with open(".token.json", "r") as tokenFile:
    KEY: Final[str] = (json.load(tokenFile))["youtubeApiToken"]
HEADER: Final[str] = "https://www.youtube.com/watch?v="

def get_movie_data(search_name, movie_num):
    """
    get data of movie in youtube in like json

    Parameters
    ----------
    search_name : str
        
    movie_num : int
        
    """

    query: str = search_name
    movie_cnt: int = movie_num + 5
    youtube: resource = build("youtube","v3",developerKey=KEY)
    response = youtube.search().list(
                q=query,
                part="id,snippet",
                maxResults = movie_cnt
    ).execute()

    i: int = 0
    while i < len(response["items"]):
        try:
            video_id: str = response["items"][i]["id"]["videoId"]
        except KeyError:
            response["items"].pop(i)
            continue
        i+=1

    while True:
        if len(response["items"]) <= movie_num:
            break
        elif len(response["items"]) > movie_num:
            response["items"].pop(len(response["items"])-1)

    return response

# return single movie name
def get_movie_name(search_name):
    response = get_movie_data(search_name, 1)
    
    name = response["items"][0]["snippet"]["title"]

    return name

# return movie name list
def get_movie_names(search_name, movie_num):
    response = get_movie_data(search_name, movie_num)
    
    names = [item["snippet"]["title"] for item in response["items"]]

    return names

# return movie url
def get_movie_url(search_name):
    datas = get_movie_data(search_name, 1)
    
    return HEADER + datas["items"][0]["id"]["videoId"]
