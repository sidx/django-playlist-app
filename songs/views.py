from django.shortcuts import render

# Create your views here.

def tracks_list(request):
	return render(request, 'songs/tracks_list.html')
	
