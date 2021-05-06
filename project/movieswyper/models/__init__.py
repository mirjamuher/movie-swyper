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
Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.
"""
