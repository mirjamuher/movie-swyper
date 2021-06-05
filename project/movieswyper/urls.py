from django.urls import path
from movieswyper.views import index, select, api

app_name = 'movieswyper'
urlpatterns = [
    path('', index.index, name='index'),
    path('select/genres', select.genres, name='select_genres'),
    path('select/movies', select.movies, name='select_movies'),
    path('select/m/movies', select.movies_mobile, name='select_movies_mobile'),
    path('api/user/movie/<int:movie_id>/rate', api.rate_movie, name='rate_movie'),
]
