from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

# add login later
def genres(request):
    context = {}
    return render(request, 'movieswyper/select_genres.html', context)

# add login later
def movies(request):
    context = {}
    return render(request, 'movieswyper/select_movies.html', context)
