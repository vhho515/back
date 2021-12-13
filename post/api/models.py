from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    body = models.TextField(max_length=360)
    year = models.IntegerField(blank=False, null=False)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()


class Movie(models.Model):
    movie = models.CharField(max_length=75)
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    critic = models.CharField(max_length=50)
    rating = models.IntegerField(blank=False, null=False)
    review = models.TextField(max_length=360)
    year = models.IntegerField(blank=False, null=False)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()


class Book(models.Model):
    book = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    reviewer = models.CharField(max_length=50)
    rating = models.IntegerField(blank=False, null=False)
    review = models.TextField(max_length=360)
    year = models.IntegerField(blank=False, null=False)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()
