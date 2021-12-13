from django.contrib import admin
from .models import Post, Movie, Book


class PostList(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'body', 'year')
    list_filter = ('title', 'category', 'author', 'year',)
    search_fields = ('title', 'category', 'author', 'body', 'year')
    ordering = ['year']


class MovieList(admin.ModelAdmin):
    list_display = ('movie', 'genre', 'director', 'critic', 'review', 'year', 'rating')
    list_filter = ('movie', 'genre', 'director', 'critic', 'year', 'rating')
    search_fields = ('movie', 'genre', 'director', 'critic', 'body', 'year')
    ordering = ['year']


class BookList(admin.ModelAdmin):
    list_display = ('book', 'genre', 'author', 'reviewer', 'year', 'rating')
    list_filter = ('book', 'genre', 'author', 'reviewer', 'rating')
    search_fields = ('book', 'genre', 'author', 'reviewer', 'year')
    ordering = ['year']


admin.site.register(Post, PostList)
admin.site.register(Movie, MovieList)
admin.site.register(Book, BookList)
