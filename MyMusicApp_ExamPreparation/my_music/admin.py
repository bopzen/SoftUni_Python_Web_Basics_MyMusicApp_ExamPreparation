from django.contrib import admin

from MyMusicApp_ExamPreparation.my_music.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'username',
        'email',
        'age'
    ]


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = [
        'album_name',
        'artist',
        'genre',
        'description',
        'image_url',
        'price'
    ]