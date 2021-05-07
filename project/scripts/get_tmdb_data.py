# To execute: $ python manage.py runscript get_tmdb_data (optional: --script-args argument_name)
# First time: $ python manage.py runscript get_tmdb_data --script-args first_time=True
# Important: Make sure adult entries are skipped

"""
7.5.2021: The plan for MVP: setup database with top 500 movies for now. Later on figure out a way to call API
for further movies and cache information in my system when required 
"""

# from movieswyper.models import TODO Import what? Everything?
import requests
from pprint import pprint #for debugging
from django.conf import settings
from movieswyper.models import Movie, Genre

def run(first_time=False):
    """
    Populates or Updates Database with TMDB Info
    """
    if first_time:
        run_first_time()
    else:
        print("You didn't activate first_time")
        # TODO: Update database regularly
        pass


def run_first_time():
    """
    Import info on top 500 english speaking movies for MVP
    Get movie/top_rated requires arg "page", 20 movies per page, aka initially need first 25 pages
    """
    url = f'https://api.themoviedb.org/3/movie/top_rated'

    response = requests.get(url, params={
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US',
        'page': 1, # change later to 25
    })

    if response.status_code != 200:
        # TODO: Might need to raise alarm for Views --> figure out how later 
        error_msg = response.get("status_message", "Something went wrong")
        print(error_msg)
    else:
        data = response.json()

        movie_list = get_movie_list(data)
        movies_imdb_ids = []

        for movie in movie_list:
            movies_imdb_ids.append(movie["id"])
        
        for entry in movies_imdb_ids:
            call_movie_API(entry)


def get_movie_list(result_dictionary):
    # uravels JSON packaging 
    for key, value in result_dictionary.items():
        if key == "results":
            return value


def call_movie_API(imdb_id):
    url=f"https://api.themoviedb.org/3/movie/{imdb_id}"
    response = requests.get(url, params={
        'api_key': settings.TMDB_API_KEY,
        'language': 'en-US',
    })

    if response.status_code != 200:
        # TODO: Might need to raise alarm for Views --> figure out how later 
        error_msg = response.get("status_message", "Something went wrong")
        print(error_msg)

    else:
        data = response.json()
        print("*"*40)
        pprint(data)

    # Works! Next step - save it into database (own internet please)
