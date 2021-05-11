from django.shortcuts import render
# Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

from movieswyper.models import Genre, Movie, Profile
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

def get_top_movies(liked_genres):
    # TODO: grab top movies from database based on liked genres. maybe movie_obj_list.extend(genre_obj.movie_set.order_by('-vote_average', '-popularity')[:int(movies_per_genre)]
    # Important: figure out the math to elegantly show 30, no matter how many genres liked
    # PROBLEM: Movies have the same tag & popularity, need to navigate around that 
    movies_shown_on_page = 30

    return Movie.objects.order_by('-vote_average', '-popularity')[:movies_shown_on_page]


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
            messages.error(request, 'Please choose at least one Genre.')
            return render(request, 'movieswyper/select_genres.html', {
                'genres': genre_obj_list,
            })
            
        genre_objs = []
        for genre in selected_genre_ids:
            try:
                genre = Genre.objects.get(id=genre)
            except (KeyError, Genre.DoesNotExist):
                messages.error(request, 'Non-Valid Genre selected. Please try again')
                return render(request, 'movieswyper/select_genres.html', {
                    'genres': genre_obj_list,
                })
            else:
                genre_objs.append(genre)
        
        # Update User Profile: clear existing genres, bulk add new ones
        crnt_user.liked_genres.clear()
        crnt_user.liked_genres.add(*genre_objs)

        # Display Success Message
        messages.success(request, 'Your profile has been updated.')
        return HttpResponseRedirect(reverse('movieswyper:select_genres'))

    # If the site is called for the first time:
    else:
        return render(request, 'movieswyper/select_genres.html', {
            'genres': genre_obj_list,
        })

# add login later
def movies(request):
    crnt_user = request.user.profile
    liked_genres = crnt_user.liked_genres.all() # TODO: Use later to adapt content to user
    movie_obj_list = get_top_movies(liked_genres)

    context = {
        'movies': movie_obj_list,
    }
    return render(request, 'movieswyper/select_movies.html', context)

def movies_mobile(request):
    crnt_user = request.user.profile
    liked_genres = crnt_user.liked_genres.all() # TODO: Use later to adapt content to user
    movie_obj_list = get_top_movies(liked_genres)

    context = {
        'movies': movie_obj_list,
    }
    return render(request, 'movieswyper/select_movies_mobile.html', context)
