from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(primary_key=True, max_length=15)
    password = models.CharField(max_length=15)
    name = models.CharField(max_length=20)
