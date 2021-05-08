from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.constraints import UniqueConstraint

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_genres = models.ManyToManyField('Genre')

"""
Below: hooking the create_user_profile and save_user_profile methods to the User model, 
whenever a save event occurs.
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class UserMovieRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_last = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['user', 'movie'], name='unique_rating'), 
        ]


"""
How to use the extended User Model:

1. When you need to access related data, prefetch it in a single database query:
users = User.objects.all().select_related('profile')

2. To access in Django Template: {{ user.profile.variablename }}

3. Access in View: user.profile.variablename

4. Forms: have two forms, one for User one for Profile in forms.py. Then in views.py, 
process both of them at the same time
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
"""
