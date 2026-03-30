from django.db import models
class Genre(models.Model):
    id = models.IntegerField
    name_en = models.CharField(max_length=20)
    name_ru = models.CharField(max_length=20)
    discription = models.CharField(max_length=40)
    def __str__(self):
        return self.name_en
    
class Track(models.Model):
    title = models.CharField(max_length=500,unique=True)
    duration = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    audio_file = models.FileField(upload_to='music/tracks/', blank=True, null=True)
    def __str__(self):
        return self.title
# Create your models here.
