from django.db import models

# Create your models here.
class Account(models.Model):
    # id = models.CharField(primary_key=True, max_length=15)
    item_name = models.CharField(max_length=15)
    date = models.CharField(max_length=64)
    io = models.CharField(max_length=20)
    kind = models.CharField(max_length=20)

class ItemKinds(models.Model):
    kind = models.CharField(primary_key=True, max_length=20)
    desc = models.CharField(max_length=20)
    color = models.CharField(max_length=20)