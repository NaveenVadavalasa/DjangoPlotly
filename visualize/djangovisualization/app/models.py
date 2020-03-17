from django.db import models

# Create your models here.

class Daily(models.Model):
    date = models.CharField(max_length=100)
    binn = models.IntegerField()
    count = models.IntegerField()

class Weekly(models.Model):
    week = models.IntegerField()
    date = models.CharField(max_length=100)
    binn = models.IntegerField()
    count = models.IntegerField()

class Monthly(models.Model):
    date = models.CharField(max_length=100)
    binn = models.IntegerField()
    count = models.IntegerField()



