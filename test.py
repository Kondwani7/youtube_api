import requests
import pandas as pd
import time
import json
from datetime import datetime, timedelta
from decouple import config
API_KEY = config("api_key")
#getting data option 1
from googleapiclient.discovery import build
youtube = build("youtube","v3", developerKey=API_KEY)

#testing out the search resource
request1 = youtube.search().list(
    part="snippet",
    type="channel",
    q="football",
)

response1 = request1.execute()
#testing out the comments resource
response2 = youtube.channels().list(
    id="UCbROEACPZuCVaAM_IzaAe1A",
    part="contentDetails"
).execute()
print(response2)
#get youtuber upload times

def get_channel(channel_name):
    return youtube.search().list(
        q=channel_name,type="channel", part="snippet",
    ).execute()

def get_videos(channel_id, part="snippet", limit=10):
    result = youtube.channels().list(
        id=channel_id,part="contentDetails"
    ).execute()
    playlist_id= result['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(
            playlistId = playlist_id,
            part=part,
            maxResults=min(limit, 50),
            pageToken=next_page_token
        ).execute()

        videos += res['items']
        next_page_token = res.get('PageToken')
        if next_page_token is None or len(videos) >= limit:
            break
        return videos



