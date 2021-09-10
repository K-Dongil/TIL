from django.shortcuts import render, redirect, get_object_or_404
from .forms import MovieForm
from .models import Movie
# Create your views here.

def create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('movies:detail', question.pk)
    else:
        form = MovieForm()
    context = {'form':form}
    return render(request, 'movies/create.html', context)

def index(request):
    movies = Movie.objects.order_by('-pk')
    
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)

def detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

def update(request , pk):
    movie =  get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance = movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)   
    else:
        form = MovieForm(instance=movie)
    context = {
        'movie':movie,
        'form':form
        }
    return render(request, 'movies/update.html', context)

def delete(request, pk):
    movie =  get_object_or_404(Movie, pk=pk)
    movie.delete()
    return redirect('movies:index')
