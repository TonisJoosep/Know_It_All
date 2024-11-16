from django.db import models


class Game(models.Model):
    points = models.CharField(max_length=20)
