from django.db import models
# from .genre import Genre --> Don't need that because Django allows you to use string-ified 
# of field/signal name and knows to look for a model with that name in the same app

class Movie(models.Model):
    # These will come from TMDB
    backdrop_path = models.CharField(max_length=255, blank=True)  # Field is allowed to be blank
    imbd_id = models.CharField(max_length=255, blank=True)
    tmdb_id = models.IntegerField(db_index=True, unique=True)
    genres = models.ManyToManyField('Genre') # Connects to Genre Model
    original_language = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255, blank=True)
    overview = models.TextField()
    popularity = models.FloatField(blank=True)
    poster_path = models.CharField(max_length=255, blank=True)
    release_date = models.DateField()
    runtime = models.IntegerField()
    tagline = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    vote_average = models.FloatField(blank=True)
    vote_count =  models.CharField(max_length=255, blank=True)

    # These are mine
    created_at = models.DateTimeField(auto_now_add=True)
    updated_last = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProductionCompany(models.Model):
    '''
    TMdb API gives list of production companies involved in movie making -->
    this might be nice information for users to sort movies by (e.g. "Pixar")
    '''
    logo_path = models.CharField(max_length=255, blank=True)
    name = models.CharField(max_length=255)
    origin_country = models.CharField(max_length=255, blank=True)
    movies_produced = models.ManyToManyField('Movie')
    

"""
{"adult":false,
"backdrop_path":"/ziC23LkMYj8gToQQYQGWSGJCLNF.jpg",
"belongs_to_collection":
    {"id":404825,
    "name":"Wreck-It Ralph Collection",
    "poster_path":"/xB6s6TGVziDuMbcIjiqgVTvnWUs.jpg",
    "backdrop_path":"/maHMw00WEuUzi4hoXxXQAGLntfH.jpg"},
"budget":165000000,
"genres":[
    {"id":10751,"name":"Family"},
    {"id":16,"name":"Animation"},
    {"id":35,"name":"Comedy"},
    {"id":12,"name":"Adventure"}],
"homepage":"http://disney.go.com/wreck-it-ralph",
"id":82690,
"imdb_id":"tt1772341",
"original_language":"en",
"original_title":"Wreck-It Ralph",
"overview":"Wreck-It Ralph is the 9-foot-tall, 643-pound villain of an arcade video game named Fix-It Felix Jr., in which the game's titular hero fixes buildings that Ralph destroys. Wanting to prove he can be a good guy and not just a villain, Ralph escapes his game and lands in Hero's Duty, a first-person shooter where he helps the game's hero battle against alien invaders. He later enters Sugar Rush, a kart racing game set on tracks made of candies, cookies and other sweets. There, Ralph meets Vanellope von Schweetz who has learned that her game is faced with a dire threat that could affect the entire arcade, and one that Ralph may have inadvertently started.",
"popularity":66.651,
"poster_path":"/zWoIgZ7mgmPkaZjG0102BSKFIqQ.jpg",
"production_companies":[
    {"id":6125,
    "logo_path":"/tVPmo07IHhBs4HuilrcV0yujsZ9.png",
    "name":"Walt Disney Animation Studios",
    "origin_country":"US"},
    {"id":2,
    "logo_path":"/wdrCwmRnLFJhEoH8GSfymY85KHT.png",
    "name":"Walt Disney Pictures","origin_country":"US"}],
"production_countries":[
    {"iso_3166_1":"US","name":"United States of America"}],
"release_date":"2012-11-01",
"revenue":471222889,
"runtime":101,
"spoken_languages":[
    {"english_name":"English",
    "iso_639_1":"en",
    "name":"English"}],
"status":"Released",
"tagline":"The story of a regular guy just looking for a little wreck-ognition.",
"title":"Wreck-It Ralph",
"video":false,
"vote_average":7.3,
"vote_count":9762
}
"""
