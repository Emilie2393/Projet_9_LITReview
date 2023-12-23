from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Ticket(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=5000)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    time_created = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    ticket = models.ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)


