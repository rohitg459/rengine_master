from django.db import models
from scanEngine.models import Notification


class SearchHistory(models.Model):
    query = models.CharField(max_length=1000)

    def __str__(self):
        return self.query


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    insert_date = models.DateTimeField()
    limit = models.IntegerField(default=0)
    notification = models.ForeignKey(
        Notification, on_delete=models.CASCADE, related_name="notification"
    )

    def __str__(self):
        return self.slug


class OpenAiAPIKey(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=500)

    def __str__(self):
        return self.key


class NetlasAPIKey(models.Model):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=500)

    def __str__(self):
        return self.key
