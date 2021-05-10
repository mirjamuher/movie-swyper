from django.shortcuts import render
# Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from movieswyper.models import Genre
from project.settings import TMDB_API_KEY
import requests

"""
Gameplan:
1. Get User Object
2. Get Genre Objects by the genre_id I'm retrieving from the homepage as chosen
3. Then link chosen Genres with User --> Careful! Delete "unselected" choices!!
4. Sasve selected Genres to database
5. show a short "Success" green box before automatically redirecting to... we'll see
7. Make sure error messages can be seen too!
"""

# FUNCTIONS HANDLING THE ORM


# ACTUAL VIEWS

@login_required
def genres(request):
    genre_obj_list = Genre.objects.all()
    crnt_user = request.user.profile

    # If form is sent:
    if request.method == 'POST':
        # Get QuearyDict of selected Genre_ids
        selected_genre_ids = request.POST.getlist('choice')

        if not selected_genre_ids:
            return render(request, 'movieswyper/select_genres.html', {  # TODO Check if that actually works
                'error_message': "Please choose at least one Genre.",
                'genres': genre_obj_list,
            })
            
        genre_objs = []
        for genre in selected_genre_ids:
            try:
                genre = Genre.objects.get(id=genre)
            except (KeyError, Genre.DoesNotExist):
                # Redisplaying form
                return render(request, 'movieswyper/select_genres.html', {  # TODO Check if that actually works
                    'error_message': "Non-Valid Genre selected. Please try again",
                    'genres': genre_obj_list,
                })
            else:
                genre_objs.append(genre)
        
        # Update User Profile: clear existing genres, bulk add new ones
        crnt_user.liked_genres.clear()
        crnt_user.liked_genres.add(*genre_objs)
        
        return HttpResponseRedirect(reverse('movieswyper:select_genres'))
        # TODO: Display Succes Message, maybe through https://docs.djangoproject.com/en/3.2/topics/http/sessions/#examples 


    # If the site is called for the first time:
    else:
        return render(request, 'movieswyper/select_genres.html', {
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
