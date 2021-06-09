from rest_framework import serializers
from videos.models import Video


# serializer to process the video data
class VideoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Video
        fields = ('__all__')