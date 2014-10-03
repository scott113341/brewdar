from django.db import models


class User(models.Model):
    email = models.EmailField()


class Device(models.Model):
    device_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    verification_token = models.CharField(max_length=16)
    verified = models.BooleanField()
    authentication_token = models.CharField(max_length=16)
    authenticated = models.BooleanField()
    user = models.ForeignKey(User)
