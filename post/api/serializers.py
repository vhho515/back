from rest_framework import serializers
from .models import Post, Movie, Book


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'category', 'title', 'author', 'body', 'year')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('pk', 'movie', 'director', 'genre', 'critic', 'rating', 'review', 'year')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('pk', 'book', 'author', 'genre', 'reviewer', 'rating', 'review', 'year')

