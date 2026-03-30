from django.shortcuts import render
from django.shortcuts import redirect
from .forms import GenreForm
from .models import Genre
from .models import Track

def index(request):
    return render(request, 'index.html')
def genre(request):
    genres = Genre.objects.all()
    return render(request, 'genre.html', {'genres': genres})
def track(request):
    tracks = Track.objects.all()
    return render(request, 'track.html', {'tracks': tracks})

def add_genre(request):
    if request.method == "POST":
        genre = GenreForm(request.POST)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    else:
        genreform = GenreForm()
        return render(request, "add_genre.html", {'form' : genreform})

def edit_genre(request, id_genre):
    g = Genre.objects.get(id = id_genre)
    if request.method == "POST":
        genre = GenreForm(request.POST, instance=g)
        if genre.is_valid():
            genre.save()
        return redirect('/genres')
    else:
        genreform = GenreForm(instance=g)
        return render(request, "edit_genre.html", {'form' : genreform})
    
def delete_genre(request, id_genre):
    genre = Genre.objects.get(id = id_genre)
    genre.delete()
    return redirect("/genres")