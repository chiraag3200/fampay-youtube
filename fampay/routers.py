from rest_framework import routers
from videos.viewsets import *

router = routers.DefaultRouter()


# route to video api's
router.register('videos', VideoViewSet, basename='videos')
