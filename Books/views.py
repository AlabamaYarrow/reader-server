from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Genre, Book, RatingVote
from .serializers import GenreSerializer, BookSerializer, VoteSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class ListGenres(APIView):
    serializer_class = GenreSerializer

    @staticmethod
    def get(self):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)


class ListBooksByGenre(APIView):
    serializer_class = BookSerializer

    @staticmethod
    def get(self):
        genre_name = self.query_params['genre_name']
        genre = Genre.objects.get(name=genre_name)
        books = Book.objects.filter(genre=genre)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class RateBook(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def post(self):
        try:
            book = self.data['book']
            vote_value = self.data['vote_value']
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            book = Book.objects.get(pk=book)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        vote = RatingVote(user=self.user, book=book, vote_value = vote_value)
        vote.save()
        serializer = VoteSerializer(vote)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

