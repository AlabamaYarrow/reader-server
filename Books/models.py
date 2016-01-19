from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=256)


class Book(models.Model):
    title = models.CharField('Title', max_length=256)
    pic = models.TextField()
    author = models.CharField('Author', max_length=256)
    description = models.TextField()
    rating = models.FloatField()
    genre = models.ForeignKey(Genre)


class RatingVote(models.Model):
    vote_value = models.IntegerField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)


