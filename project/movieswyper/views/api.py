import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from movieswyper.models import Genre, Movie, Profile, UserMovieRating

@login_required
@csrf_exempt
def rate_movie(request, movie_id):
    payload = json.loads(request.body)
    rating = payload.get("rating")
    user = request.user

    # Validation Process
    if movie_id:
        try:
            movie_obj = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return JsonResponse({"error":"Invalid Movie Selected"}, status=400)
    else:
        return JsonResponse({"error":"No Movie Selected"}, status=400)

    if not rating or not isinstance(rating, int) or rating not in [1, 2, 3]:
        return JsonResponse({"error":"Invalid Rating"}, status=400)

    # Update Movie Rating
    movie = Movie.objects.get(pk=movie_id)

    rating_obj, created = UserMovieRating.objects.update_or_create(
        user = user,
        movie = movie,
        defaults = {'rating': rating},
    )

    return JsonResponse({})
