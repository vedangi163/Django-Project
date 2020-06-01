from django.urls import path
from django.urls import include, re_path
from . import views


app_name = 'music'
urlpatterns = [
    #/music/
    path('', views.IndexView.as_view(), name='index'),

    re_path(r'songlist/$', views.songIndexView.as_view(), name='songlist'),
    re_path(r'register/$', views.UserFormView.as_view(), name='register'),
     #/music/2345
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #/music/album/add/
    re_path(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    #/music/album/2/
    re_path(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    #/music/album/2/delete/
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
    #/music/2/add/
    re_path(r'^(?P<pk>[0-9]+)/addsong/$', views.SongCreate.as_view(), name='song-add'),

    re_path(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),

    re_path(r'^(?P<album_id>[0-9]+)/favorite_song/(?P<song_id>[0-9]+)/$', views.favorite_song, name='favorite_song'),

    re_path(r'^(?P<album_id>[0-9]+)/delete_song_allsongs/(?P<song_id>[0-9]+)/$', views.delete_song_allsongs, name='delete_song_allsongs'),

    re_path(r'^(?P<album_id>[0-9]+)/favorite_song_allsongs/(?P<song_id>[0-9]+)/$', views.favorite_song_allsongs, name='favorite_song_allsongs'),


]





