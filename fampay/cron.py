from videos.models import Video
from django.conf import settings
import requests


# this function is run every 1 minute using crontab and it hits the API to fetch the new videos and save them to the database
def fetch_videos():
    
    # default time if no video is present in the database
    publishedAfter = settings.PUBLISHING_START_TIME

    # find the publish time of the latest video
    if Video.objects.exists():
        publishedtime = Video.objects.latest('publishing_datetime').publishing_datetime
        if publishedtime:
            publishedAfter = publishedtime


    # url to fetch the videos with published after publishedAfter with some other pre-required parameters
    url = f'https://www.googleapis.com/youtube/v3/search?key={settings.KEY}&q={settings.SEARCH_QUERY}&order={settings.ORDER_BY}&type={settings.TYPE}&publishedAfter={publishedAfter}&part={settings.PART}&maxResults={settings.MAX_RESULTS}'
    try:
        res = requests.get(url)
        results = res.json()
    except Exception as e:
        print(e)
        results = []
        pass


    # function the fetch and save all the videos as only 50 videos are fetched at a time
    while True:
        # find the token of the next page if there are some fetched results on the next page 
        if 'nextPageToken' in results:
            nextPageToken = results['nextPageToken']
        else:
            nextPageToken = None


        # create new objects
        results = results['items']
        for item in results:
            title = item['snippet']['title']
            description = item['snippet']['description']
            publishing_datetime = item['snippet']['publishedAt']
            thumbnails = item['snippet']['thumbnails']
            video_id = item['id']['videoId']
            Video.objects.create(title = title, description = description, publishing_datetime = publishing_datetime,thumbnails = thumbnails, video_id = video_id)


        # ''' if there are no more results and we have saves all of them, we stop fetchig and saving'''
        if nextPageToken is None:
            break


        # ''' url to fetch videos on the next page with next page token provided as nextPageToken'''
        url = f'https://www.googleapis.com/youtube/v3/search?key={settings.KEY}&pageToken={nextPageToken}&q={settings.SEARCH_QUERY}&order={settings.ORDER_BY}&type={settings.TYPE}&part={settings.PART}&maxResults={settings.MAX_RESULTS}'
        

        # '''fetching the results'''
        results = []
        try:
            res = requests.get(url)
            results = res.json()
        except Exception as e:
            print(e)
            pass

