from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer


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


class BookViewSet(ViewSet):

    def create(self):
        # add lo list
        pass

    def update(self):
        # mark as read
        pass

    def delete(self):
        # delete from list
        pass