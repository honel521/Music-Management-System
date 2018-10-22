from django import forms
from django.contrib.auth.models import User

from .models import Playlist, Song


class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ['title', 'image','user']

class AddSongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['album', 'song_title', 'audio_file', 'part_of_playlist']
