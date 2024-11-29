from django.contrib.auth.models import User
from django.db import models


DIFFICULTY_CHOICES = {
    'E': 'Easy',
    'M': 'Medium',
    'H': 'Hard',
}


class Game(models.Model):
    points = models.IntegerField(default=0, null=False, blank=False)
    category = models.CharField(null=True, blank=True, max_length=64)
    difficulty = models.CharField(
        null=False,
        blank=False,
        choices=DIFFICULTY_CHOICES,
        default=DIFFICULTY_CHOICES['M'],
        max_length=16,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.category} - {self.difficulty} - {self.user}'


class GameHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=64, null=True, blank=True)
    difficulty = models.CharField(choices=DIFFICULTY_CHOICES.items(), max_length=16)
    score = models.IntegerField(default=0)
    date_played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.difficulty} - {self.score} on {self.date_played}"