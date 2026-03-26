from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone_no = models.PositiveBigIntegerField()
    REQUIRED_FIELDS = ['email', 'phone_no']
