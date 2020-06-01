
from django.urls import reverse
from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length = 500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def __str__(self):
        return self.album_title

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)
    audio_file = models.FileField(default='')

    def get_absolute_url(self):
        a = self.album
        return reverse('music:detail', kwargs={'pk' : a.pk})

    def __str__(self):
        return self.song_title
