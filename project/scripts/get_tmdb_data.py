# To execute: $ python manage.py runscript get_tmdb_data (optional: --script-args argument_name)
# First time: $ python manage.py runscript get_tmdb_data --script-args first_time=True

"""
7.5.2021: The plan for MVP: setup database with top 500 movies for now. Later on figure out a way to call API
for further movies and cache information in my system when required 
"""

import requests
from pprint import pprint #for debugging
from django.conf import settings
from movieswyper.models import Movie, Genre, ProductionCompany

def run(first_time=False):
    """
    Populates or Updates Database with TMDB Info
    """
    if first_time:
        pages = 25 # Set how many of the top pages you want
        for page_no in range(1, pages+1):
            print("*"*40)
            print(f"You are calling the API for page number {page_no}")
            run_first_time(page_no)
    else:
        print("You didn't activate first_time")
        # TODO: Update database regularly
        pass


def run_first_time(page_no):
    """
    Import info on top 500 english speaking movies for MVP
    Get movie/top_rated requires arg "page", 20 movies per page, aka initially need first 25 pages
    """
    url = f'https://api.themoviedb.org/3/movie/top_rated'

    response = requests.get(url, params={
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US',
        'page': page_no,
    })

    if response.status_code != 200:
        # TODO: Might need to raise alarm for Views --> figure out how later 
        error_msg = response.get("status_message", "Something went wrong")
        print(error_msg)
    else:
        data = response.json()

        movie_list = get_movie_list(data)
        movies_tmdb_ids = []

        for movie in movie_list:
            # If the movie is not pornographic, add its id to the list 
            if movie["adult"] == False:
                movies_tmdb_ids.append(movie["id"])
        
        for entry in movies_tmdb_ids:
            # For each entry in the list, call the individual movie API
            # to get full information for the population of database
            call_movie_API(entry)


def get_movie_list(result_dictionary):
    # uravels JSON packaging 
    for key, value in result_dictionary.items():
        if key == "results":
            return value


def call_movie_API(tmdb_id):
    url=f"https://api.themoviedb.org/3/movie/{tmdb_id}"
    response = requests.get(url, params={
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US',
    })

    if response.status_code != 200:
        error_msg = response.get("status_message", "Something went wrong")
        print(error_msg)

    else:
        data = response.json()
        # Update or Create Movie Object
        movie_obj, created = Movie.objects.update_or_create(
            tmdb_id=data['id'],
            defaults = {
                'backdrop_path': data['backdrop_path'],
                'imbd_id': data['imdb_id'],
                'original_language': data['original_language'],
                'original_title': data['original_title'],
                'overview': data['overview'],
                'popularity': data['popularity'],
                'poster_path': data['poster_path'],
                'release_date': data['release_date'],
                'runtime': data['runtime'],
                'tagline': data['tagline'],
                'title': data['title'],
                'vote_average': data['vote_average'],
                'vote_count': data['vote_count'],
            }
        )
        
        # Connect Movie Object to relevant Genres (exist through get_genre_data.py)
        for genre in data['genres']:
            tmdb_id = genre['id']
            genre_obj = Genre.objects.get(tmdb_id=tmdb_id)
            genre_obj.movie_set.add(movie_obj)

        # Connect Movie Object to Production Companies (optional: create PC Object)
        for pc in data['production_companies']:
            tmdb_id = pc['id']

            pc_obj, created = ProductionCompany.objects.update_or_create(
                tmdb_id = tmdb_id,
                defaults = {
                        'logo_path': pc['logo_path'],
                        'name': pc['name'],
                        'origin_country': pc['origin_country'],
                }
            )

            movie_obj.productioncompany_set.add(pc_obj)


    # TODO: Populate database with 1 (!) movie. Then, do it again to see if the update_or_create works. 
    # Only then, let the whole first 25 pages run through (own internet)

    # Works! Next step - save it into database (own internet please)
    # You want to try and get the existing object by the ID, and if it doesn't exist, 
    # create a blank object. then, overwrite the fields on the object, then save the object. 
    # that way, you have "create or update" semantics
    # https://docs.djangoproject.com/en/3.2/ref/models/querysets/#get-or-create
