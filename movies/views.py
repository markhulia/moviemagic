from django.shortcuts import get_object_or_404, render

from .models import Movie


def index(request):
    latest_movies = Movie.objects.order_by('title')

    context = {
        'latest_movies': latest_movies
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    # response = '{} {} {} {}'.format(movie.title, movie.release_year, movie.user_rating,
    #                                 str([g for g in movie.genre_set.all()]))
    return render(request, 'movies/detail.html', {'movie': movie})
