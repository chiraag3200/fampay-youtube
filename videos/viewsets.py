from rest_framework import viewsets
from videos.serializers import VideoSerializer
from .models import Video
from django.db.models import Q


# viewset to respond to Video API's
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    # function to return results to search video api
    def get_queryset(self):
        query = self.request.query_params.get("query", None)
        if query:
            queryset = Video.objects.filter(Q(title__icontains = query) | Q(description__icontains=query)).order_by('-publishing_datetime')
        else:
            queryset = Video.objects.all().order_by('-publishing_datetime')
        return queryset


    # function to return results to get videos api
    def retrieve(self, request, pk=None):
        queryset = Video.objects.all().order_by('-publishing_datetime')
        return queryset
