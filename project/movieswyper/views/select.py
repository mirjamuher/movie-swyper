from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

from movieswyper.models import Genre
from project.settings import TMDB_API_KEY

# add login later
def genres(request):

    genre_obj_list = Genre.objects.all()

    return render(request, 'movieswyper/select_genres_new.html', {
        'genres': genre_obj_list,
    })

"""
Genre info:
{"genres":[
{"id":28,"name":"Action"},
{"id":12,"name":"Adventure"},
{"id":16,"name":"Animation"},
{"id":35,"name":"Comedy"},
{"id":80,"name":"Crime"},
{"id":99,"name":"Documentary"},
{"id":18,"name":"Drama"},
{"id":10751,"name":"Family"},
{"id":14,"name":"Fantasy"},
{"id":36,"name":"History"},
{"id":27,"name":"Horror"},
{"id":10402,"name":"Music"},
{"id":9648,"name":"Mystery"},
{"id":10749,"name":"Romance"},
{"id":878,"name":"Science Fiction"},
{"id":10770,"name":"TV Movie"},
{"id":53,"name":"Thriller"},
{"id":10752,"name":"War"},
{"id":37,"name":"Western"}
]}
"""

# add login later
def movies(request):
    context = {}
    return render(request, 'movieswyper/select_movies.html', context)
