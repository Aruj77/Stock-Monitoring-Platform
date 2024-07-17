from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(
        max_length=100
    )  # For simplicity, use hashed passwords in real-world scenarios


class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(
        max_length=10
    )  # Assuming stock symbols are alphanumeric and not too long
