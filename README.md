# movie-swyper
Take the questions out of movie night suggestions!

To be edited as the project evolves.

Credits
The Movie Database API https://developers.themoviedb.org/3/getting-started/introduction 
Color Scheme: https://themestr.app/

Installation Instructions (rough notes)
1. create venv
2. install dependencies: $ pip install -r requirements.txt
3. install npm dependencies
4. Get an API Key with Movie Database API and make file local_settings.py with Global Variable saving it

To populate the database locally, run the following commands:
$ python manage.py runscript get_genre_data --script-args first_time=True
Careful: check get_tmdb_data.py and configure how many movies you want to pull from TMDb, can be time & ressource consuming
