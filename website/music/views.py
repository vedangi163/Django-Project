from django.views import generic
from .models import Album, Song
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.views.generic import View

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'
    def get_queryset(self):
        return Album.objects.all()


class songIndexView(generic.ListView):
    template_name = 'music/songlist.html'
    context_object_name = 'all_songs'
    def get_queryset(self):
        return Song.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')

class SongCreate(CreateView):
    model = Song
    fields = ['song_title', 'audio_file']

    def form_valid(self, form):
        album = get_object_or_404(Album, pk = self.kwargs['pk'])
        form.instance.album = album
        return super(SongCreate, self).form_valid(form)

def delete_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/detail.html', {'album': album})


def favorite_song(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk= song_id)
    if song.is_favorite:
        song.is_favorite= False
    else:
        song.is_favorite = True
    song.save()
    return render(request, 'music/detail.html', {'album': album})


def delete_song_allsongs(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/songlist.html', {'all_songs': Song.objects.all()})



def favorite_song_allsongs(request, album_id, song_id):
    album = get_object_or_404(Album, pk=album_id)
    song = Song.objects.get(pk= song_id)
    if song.is_favorite:
        song.is_favorite= False
    else:
        song.is_favorite = True
    song.save()
    return render(request, 'music/songlist.html', {'all_songs': Song.objects.all()})

class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('music:index')

        return render(request, self.template_name, {'form': form})

