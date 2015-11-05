from django.db import models


class ReaderUser(models.Model):
    CompletedBooks = models.ManyToManyField('Books.Book')
