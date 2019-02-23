from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200)
    title_type = models.CharField(max_length=200)
    release_date = models.DateTimeField('date released')
    user_rating = models.IntegerField(default=5, validators=[MaxValueValidator(10),
                                                             MinValueValidator(0)])
    vote_count = models.IntegerField(default=1000, validators=[MinValueValidator(100)])
    genre = models.CharField(max_length=200)
