from django.contrib import admin
from .models import Movie, Genre, Profile, ProductionCompany, UserMovieRating

# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Profile)
admin.site.register(ProductionCompany)
admin.site.register(UserMovieRating)
