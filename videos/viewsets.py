from rest_framework import viewsets
from videos.serializers import VideoSerializer
from .models import Video
from django.db.models import Q
import re


# viewset to respond to Video API's
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    # function to return results to search video api
    def get_queryset(self):

        # search query entered by the user
        query = self.request.query_params.get("query", None)               
        queryset = []

        # if the user has not entered any search query
        if not query:
            queryset = Video.objects.all().order_by('-publishing_datetime')
            return queryset

        # if the user has entered a search query
        ################## Optimised search api to search videos containing partial match for the search query in either video title or description.####################
        updated_queryset = []
        query = query.split(" ")

        # find all videos which partial match with the search query
        for item in query:
            queryset = Video.objects.filter(Q(title__icontains = item) | Q(description__icontains=item))
            for video in queryset:
                updated_queryset.append(video)

        # find all videos with fully match with the query entered in any order
        final_queryset = []
        for video in updated_queryset:
            count_in_title = 0
            count_in_description = 0
            for item in query:
                #sub query is present in title
                if re.search(item, video.title, re.IGNORECASE):                                    
                    count_in_title += 1

                # sub query is present in description
                if re.search(item, video.description, re.IGNORECASE):                              
                    count_in_description += 1 

            # query is present in title or description
            if count_in_title == len(query) or count_in_description == len(query):                 
                if video not in final_queryset:
                    final_queryset.append(video)

        return final_queryset


    # function to return results to get videos api
    def retrieve(self, request, pk=None):
        queryset = Video.objects.all().order_by('-publishing_datetime')
        return queryset
