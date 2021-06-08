from django.db import models
from djangodeletes.softdeletes import SoftDeletable, SoftDeleteQuerySet, SoftDeleteManager
from django.contrib.postgres.fields import JSONField

class Video(SoftDeletable, models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, null=True, blank=True)
    publishing_datetime = models.DateTimeField(null=True, blank=True)
    thumbnails = JSONField(null=True)
    video_id = models.CharField(max_length=50, null=True, blank=True)

    objects = SoftDeleteManager.from_queryset(SoftDeleteQuerySet)()

    def __str__(self):
        return str(self.title)
