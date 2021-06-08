from rest_framework import routers
from videos.viewsets import *

router = routers.DefaultRouter()

router.register('videos', VideoViewSet, basename='videos')
