from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_type = models.CharField(max_length=200)
    release_date = models.CharField(max_length=20)
    user_rating = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                             MinValueValidator(0)])
    vote_count = models.IntegerField(default=1000, validators=[MinValueValidator(100)])


class Genre(models.Model):
    """
    Since one movie can have multiple genres, this can be expressed as
    one-to-many relationship between movie and genre
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)
