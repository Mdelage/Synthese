# coding=utf-8
from django.db import models


# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=120, verbose_name="nom de l'artiste")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "artiste"


class Album(models.Model):
    title = models.CharField(max_length=160, verbose_name="titre de l'album")
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, verbose_name="artiste")

    def __str__(self):
        return self.title


class Track(models.Model):
    name = models.CharField(max_length=200, verbose_name="nom")
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name="tracks")
    composer = models.CharField(max_length=220, verbose_name="compositeur")
    milliseconds = models.TextField(verbose_name="durée")
    bytes = models.PositiveIntegerField()
    unitPrice = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="prix unitaire")

    def __str__(self):
        return self.name
