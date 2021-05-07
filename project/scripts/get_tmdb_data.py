# To execute: $ python manage.py runscript get_tmdb_data.py (optional: --script-args argument_name)

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
    #TODO: Change page to 1
    """
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={settings.TMDB_API_KEY}&language=en-US&page=1'
    response = requests.get(url)

    if response.status_code != 200:
        # TODO: Might need to raise alarm for Views --> figure out how later 
        if response["status_message"]:
            error_msg = response["status_message"]
        else: 
            error_msg = "Something went wrong"
        print(error_msg)
    else:
        data = response.json()

        movie_list = get_movie_list(data)
        for movie in movie_list:
            print(movie["title"])

def get_movie_list(result_dictionary):
    for key, value in result_dictionary.items():
        if key == "results":
            return value
