from django.db import models


from django.contrib.auth.models import AbstractUser

class UserAuth(AbstractUser):
    city = models.CharField(max_length=50)