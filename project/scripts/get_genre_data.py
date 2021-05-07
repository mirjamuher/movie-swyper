# To execute: $ python manage.py runscript get_genre_data (optional: --script-args argument_name) or
# $ python manage.py runscript get_genre_data --script-args first_time=True


import requests
from pprint import pprint #for debugging
from django.conf import settings
from movieswyper.models import Movie, Genre

def run(first_time=False):
    if first_time:
        run_first_time()
    else:
        # TODO: Update function
        pass

def run_first_time():
    url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={settings.TMDB_API_KEY}&language=en-US"
    response = requests.get(url)

    if response.status_code != 200:
        if response["status_message"]:
            error_msg = response["status_message"]
        else: 
            error_msg = "Something went wrong"
        print(error_msg)
    else:
        data = response.json()
        genre_list = get_genre_list(data)
        for genre in genre_list:
            # TODO: Next step - save it into the database
            print(f"id is {genre['id']}")
            print(f"name is {genre['name']}")
            print('******')

def get_genre_list(result_dictionary):
    for key, value in result_dictionary.items():
        if key == "genres":
            return value

