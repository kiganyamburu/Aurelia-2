from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    spotify_id = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)

class Follower(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
