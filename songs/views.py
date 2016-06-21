from django.shortcuts import render, get_object_or_404

from .models import songModel, genreModel

# Create your views here.

def tracks_list(request):
	allTracks = songModel.objects.filter()
	return render(request, 'songs/tracks_list.html',{'allTracks':allTracks})
	
def genre_list(request):
	allGenres = genreModel.objects.filter()
	return render(request, 'songs/genres_list.html',{'allGenres':allGenres})
	
def track_detail(request,id):
	print id
	track = songModel.objects.get(id=id)
	return render(request, 'songs/track_detail.html',{'track':track})

def genre_detail(request,id):
	print id
	genre = genreModel.objects.get(id=id)
	return render(request, 'songs/genre_detail.html',{'genre':genre})
