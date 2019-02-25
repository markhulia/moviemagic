from django.http import HttpResponse
from .models import Movie


def index(request):
    latest_movies = Movie.objects.order_by('title')
    response = ', '.join([str((m.title, m.title_type, m.release_year, m.user_rating,
                               [g for g in m.genre_set.all()])) for m in latest_movies])
    return HttpResponse(response)


def detail(request, movie_id):
    response = "Movie: {}".format(movie_id)
    return HttpResponse(response)


