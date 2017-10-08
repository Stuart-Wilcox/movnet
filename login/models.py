from django.db import models


class Session(models.Model):
    username = models.CharField(max_length=150, unique=True)
    client_token = models.CharField(max_length=150)
    max_age = models.IntegerField()
    creation_age = models.BigIntegerField()
