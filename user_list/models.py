from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/')
