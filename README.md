# Project Goal

To make an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.

# Tasks Completed

- Server calls the YouTube API continuously in background (async) using cronjob after every 1 minute for fetching the latest videos for a predefined search query and stores the data of videos in the database.

- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.

- A basic search API to search the stored videos using their title and description.

- An optimises search api, so that it's able to search videos containing partial match for the search query.
  Ex : A video with title 'How to make tea?' should match for the search query 'tea how'
  
 # How To Run the Project
 
Run `sudo docker-compose up` for dev server.

Run `python3 manage.py crontab add .` to run the cronjob in the background to fetch the latest videos.

Navigate to `http://localhost:8000/admin`.

Superuser Credentials:
username : admin
password : admin#123

# How To Test the Project
GET API End Point : http://localhost:8000/api/videos
Search API End Point : http://localhost:8000/api/videos/?query=cricket
