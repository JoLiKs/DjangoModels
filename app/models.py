from django.db import models

class users(models.Model):
    login = models.TextField()
    password = models.TextField()

class users2(models.Model):
    login2 = models.TextField()
    password2 = models.OneToOneField(users, on_delete=models.CASCADE, primary_key=True)


class users3(models.Model):
   us = models.ManyToManyField(users)