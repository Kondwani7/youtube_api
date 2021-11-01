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
response2 = youtube.comments().list(
    id="l0U7SxXHkPY",
    part="snippet"
).execute
#get youtuber upload times
