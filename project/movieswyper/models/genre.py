from django.db import models

class Genre(models.Model):
    # From TMDB
    name = models.CharField(max_length=255)

    # Mine
    created_at = models.DateTimeField(auto_now_add=True)
    updated_last = models.DateTimeField(auto_now=True)
