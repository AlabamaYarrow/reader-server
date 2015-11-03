from django.db import models
from Books.models import Book


class ReaderUser(models.Model):
    CompletedBooks = models.ManyToManyField(Book)
