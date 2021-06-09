from videos.models import Video
from django.conf import settings
import requests
import aiohttp
import asyncio

url = f'https://www.googleapis.com/youtube/v3/search?key={settings.KEY}&q={settings.SEARCH_QUERY}&order={settings.ORDER_BY}&type={settings.TYPE}&publishedAfter={settings.PUBLISHING_START_TIME}&part={settings.PART}&maxResults={settings.MAX_RESULTS}'

def fetch_videos():
    Video.objects.create(title = 'aa')
    res = requests.get(url)
    results = res.json()['items']
    for item in results:
        title = item['snippet']['title']
        description = item['snippet']['description']
        publishing_datetime = item['snippet']['publishedAt']
        thumbnails = item['snippet']['thumbnails']
        video_id = item['id']['videoId']
        is_video_present = Video.objects.filter(video_id = video_id).first()
        if not is_video_present:
            Video.objects.create(title = title, description = description, publishing_datetime = publishing_datetime,thumbnails = thumbnails, video_id = video_id)
