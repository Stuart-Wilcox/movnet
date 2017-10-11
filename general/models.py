from django.db import models
from django.contrib.auth.models import User as django_user


class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    cost = models.FloatField()
    length = models.IntegerField()
    rating = models.IntegerField()
    cast_list = models.CharField(max_length=1000)
    datetime = models.DateTimeField()
    movie_poster = models.CharField(max_length=500)  # url to movie poster for now

    def __str__(self):
        return 'Movie: %s' % self.name


class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    favourite_movies = models.ManyToManyField(Movie, related_name='favourite_movies')
    movie_wishlist = models.ManyToManyField(Movie, related_name='movie_wishlist')

    def add_favourite(self, movie):
        self.favourite_movies.add(movie)
        self.save()
        movie.save()

    def remove_favourite(self, movie):
        self.favourite_movies.remove(movie)
        self.save()
        movie.save()

    def add_wishlist(self, movie):
        self.movie_wishlist.add(movie)
        self.save()
        movie.save()

    def remove_wishlist(self, movie):
        self.movie_wishlist.remove(movie)
        self.save()
        movie.save()

    def __str__(self):
        return 'User: %s' % self.username


class Theatre(models.Model):
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    movies = models.ManyToManyField(Movie, related_name='available_movies')

    def add_movie(self, movie):
        self.movies.add(movie)
        self.save()
        movie.save()

    def remove_movie(self, movie):
        self.movies.remove(movie)
        self.save()
        movie.save()

    def __str__(self):
        return "Theatre: %s" % self.name

class Event(models.Model):
    name = models.CharField(max_length=500)
    datetime = models.DateTimeField()
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='event_users')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def add_user(self, user):
        self.users.add(user)
        self.save()
        user.save()

    def remove_user(self, user):
        self.users.remove(user)
        self.save()
        user.save()

    def add_users(self, users):
        for user in users:
            self.add_user(user)

    def __str__(self):
        return 'Event: %s' % self.name