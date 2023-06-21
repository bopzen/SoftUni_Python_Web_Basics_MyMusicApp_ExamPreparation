from django.urls import path, include

from MyMusicApp_ExamPreparation.my_music.views import show_home, add_album, album_details, edit_album, delete_album, \
    profile_details, delete_profile

urlpatterns = [
    path('', show_home, name='show-home'),
    path('album/', include([
        path('add/', add_album, name='add-album'),
        path('details/<int:pk>/', album_details, name='details-album'),
        path('edit/<int:pk>/', edit_album, name='edit-album'),
        path('delete/<int:pk>/', delete_album, name='delete-album')
    ])),
    path('profile/', include([
        path('details/', profile_details, name='details-profile'),
        path('delete/', delete_profile, name='delete-profile')
    ]))
]