from django.contrib.auth.models import User
from django.db import models

GAME_TYPE_CHOICES = {
    "TF": "True/False",
    "MC": "Multiple choices",
}
DIFFICULTY_CHOICES = {
    "E": "Easy",
    "M": "Medium",
    "H": "Hard",
}


class Game(models.Model):
    points = models.IntegerField(default=0, null=False, blank=False)
    type = models.CharField(
        null=False,
        blank=False,
        choices=GAME_TYPE_CHOICES,
        default=GAME_TYPE_CHOICES["MC"],
        max_length=32,
    )
    category = models.CharField(null=True, blank=True, max_length=64)
    difficulty = models.CharField(
        null=False,
        blank=False,
        choices=DIFFICULTY_CHOICES,
        default=DIFFICULTY_CHOICES["M"],
        max_length=16,
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.category} - {self.difficulty} - {self.user}"


