from .genre import Genre
from .movie import Movie, ProductionCompany
from .profile import Profile, UserMovieRating


"""
This file allows Python to import an entire directory through the definition of __all__ 
This is important when creating the database folder, as Django aka the ORM want to access
the entire directory when creating/updating Databases
p.s. not needed in views because I import the files there directly, not the entire directory
"""

__all__ = [
    'Movie',
    'ProductionCompany',
    'Genre',
    'Profile',
    'UserMovieRating',
]


"""
three-step guide to making model changes:

Change your models (in models).
$ python manage.py makemigrations --> create migrations for those changes
$ python manage.py migrate --> apply those changes to the database.
"""
