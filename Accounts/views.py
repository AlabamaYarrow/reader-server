from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from Books.serializers import BookSerializer
from Books.models import Book
from .models import ReaderUser


class BookViewSet(ViewSet):
    """
    GET (list): list users books.
    POST (create): add book to list.
    PUT (update): mark as read.
    DELETE (destroy): remove from list.
    """

    permission_classes = (IsAuthenticated,)

    @staticmethod
    def list(self):
        try:
            user = User.objects.get(pk=self.query_params['user'])
            reader = ReaderUser.objects.get(user=user)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        completed_books = reader.completed_books
        planned_books = reader.planned_books
        data = {
            'planned_books': BookSerializer(planned_books, many=True).data,
            'completed_books': BookSerializer(completed_books, many=True).data
            }
        return Response(data=data, status=status.HTTP_200_OK)

    @staticmethod
    def create(self):
        try:
            reader = ReaderUser.objects.get(user=self.user)
        except ObjectDoesNotExist:
            reader = ReaderUser(user=self.user)
            reader.save()
        try:
            book = Book.objects.get(pk=self.data['book'])
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reader.planned_books.add(book)
        reader.save()

        return Response(status=status.HTTP_201_CREATED)

    @staticmethod
    def update(self, pk):
        reader = ReaderUser.objects.get(user=self.user)
        try:
            book = Book.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reader.planned_books.remove(book)
        reader.completed_books.add(book)
        reader.save()
        return Response(status=status.HTTP_200_OK)

    @staticmethod
    def destroy(self, pk):
        reader = ReaderUser.objects.get(user=self.user)
        try:
            book = Book.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reader.completed_books.remove(book)
        reader.save()
        return Response(status=status.HTTP_200_OK)
