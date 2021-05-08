"""
Edit abilities of admin view: https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#django.contrib.admin.register
Will be convenient for users later on!
"""

from django.contrib import admin
from .models import Movie, Genre, Profile, ProductionCompany, UserMovieRating

admin.site.register(Genre)
admin.site.register(Profile)
admin.site.register(ProductionCompany)
admin.site.register(UserMovieRating)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'popularity', 'vote_average')
    ordering = ('vote_average', 'popularity')
    search_fields = ('title', 'genres__name', 'productioncompany__name')
