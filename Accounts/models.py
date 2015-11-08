from django.db import models
from django.contrib.auth.models import User


class ReaderUser(models.Model):
    user = models.ForeignKey(User)
    planned_books = models.ManyToManyField('Books.Book', related_name='planned_books')
    completed_books = models.ManyToManyField('Books.Book', related_name='completed_books')
