from django.shortcuts import render
from .models import Playlist

def home(request):
    playlists = Playlist.objects.all()
    return render(request, 'music/player.html', {'playlists': playlists})

def playlist_detail(request, id):
    playlist = Playlist.objects.get(id=id)
    return render(request, 'music/playlist.html', {'playlist': playlist})
