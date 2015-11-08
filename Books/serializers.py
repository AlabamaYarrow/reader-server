from rest_framework import serializers
from .models import Genre, Book, RatingVote


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name',)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'pic', 'description', 'rating')


class VoteSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = RatingVote
        fields = ('vote_value', 'user', 'book')
