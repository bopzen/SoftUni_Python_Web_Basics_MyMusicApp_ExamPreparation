from django.http import HttpResponse
from django.shortcuts import render, redirect

from MyMusicApp_ExamPreparation.my_music.forms import ProfileForm, AlbumForm, AlbumDeleteForm, ProfileDeleteForm
from MyMusicApp_ExamPreparation.my_music.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()
    except:
        return None


def show_home(request):
    profile = get_profile()
    if profile is None:
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('show-home')
        context = {
            'profile': profile,
            'form': form
        }
        return render(request, 'home-no-profile.html', context)

    albums = Album.objects.all()
    context = {
        'profile': profile,
        'albums': albums
    }
    return render(request, 'home-with-profile.html', context)


def add_album(request):
    profile = get_profile()
    form = AlbumForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('show-home')
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'add-album.html', context)


def album_details(request, pk):
    album = Album.objects.filter(pk=pk).get()
    context = {
        'album': album
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show-home')
    context = {
        'form': form,
        'album': album
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show-home')
    context = {
        'form': form,
        'album': album
    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.count()

    context = {
        'profile': profile,
        'albums_count': albums_count
    }

    return render(request, 'profile-details.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show-home')
    context = {
        'form': form
    }
    return render(request, 'profile-delete.html', context)