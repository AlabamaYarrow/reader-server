from django.db import models
from Accounts.models import ReaderUser


class Book(models.Model):
    title = models.CharField('Title', max_length=256)
    pic = models.ImageField()
    author = models.CharField('Author', max_length=256)
    description = models.TextField()
    rating = models.IntegerField()
    genre = models.ForeignKey(Genre)


class RatingVote(models.Model):
    value = models.IntegerField()
    user = models.ForeignKey(ReaderUser)
    book = models.ForeignKey(Book)


class Genre(models.Model):
    name = models.CharField(max_length=256)
