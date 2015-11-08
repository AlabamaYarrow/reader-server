from django.db import models
from Accounts.models import ReaderUser
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=256)


class Book(models.Model):
    title = models.CharField('Title', max_length=256)
    pic = models.CharField('Pic', max_length=256)
    author = models.CharField('Author', max_length=256)
    description = models.TextField()
    rating = models.FloatField()
    genre = models.ForeignKey(Genre)


class RatingVote(models.Model):
    vote_value = models.IntegerField()
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)


