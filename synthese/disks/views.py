# coding=utf-8
from django.shortcuts import render, get_object_or_404
from .models import Album


# Create your views here.

def album(request, id_album):
    # objet représentant tous les albums
    all_albums = Album.objects.all()
    # objet représentant l'album correspondant à id_album
    current_album = get_object_or_404(Album, id=id_album)
    # objet correspondant à tous les tracks de l'album
    tracks = current_album.tracks.all()

    # conversion de la durée en minutes
    for track in tracks:
        track.milliseconds = int(track.milliseconds) / 1000
        minutes = int(track.milliseconds // 60)
        secondes = int(track.milliseconds % 60)
        track.milliseconds = "{0} m {1} s".format(minutes, secondes)

    # conversion de la taille en MB
    for track in tracks:
        track.bytes = round(track.bytes / 1000000, 2)

    # objet correspondant à l'artiste ayant fait l'album
    artist = current_album.artist

    return render(request, "disks/albums.html", locals())
