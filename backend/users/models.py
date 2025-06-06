from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Puedes agregar campos personalizados aquí
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Otros campos de perfil
    bio = models.TextField(blank=True, null=True)
