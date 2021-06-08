from rest_framework import viewsets
from videos.serializers import VideoSerializer
from .models import Video



class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def retrieve(self, request, pk=None):
        queryset = Video.objects.all().order_by('publishing_datetime')
        return queryset
