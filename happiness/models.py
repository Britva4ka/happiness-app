from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Member(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.username


class Happiness(models.Model):
    LEVEL_CHOICES = (
        ("1", "Joy"),
        ("2", "Excitement"),
        ("3", "Gratitude"),
        ("4", "Pride"),
        ("5", "Optimism"),
        ("6", "Contentment"),
        ("7", "Love")
    )
    happiness_level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True, null=False)

    def __str__(self):
        return f'{self.happiness_level}, {self.date}'
