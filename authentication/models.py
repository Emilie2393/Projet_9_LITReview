
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    username = models.CharField(max_length=30, unique=True, verbose_name="Utilisateur")
    follows = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='suit'
    )
    followed_by = models.ManyToManyField(
        'self',
        symmetrical=False,
        verbose_name='vous suit',
        related_name="followers"
    )

