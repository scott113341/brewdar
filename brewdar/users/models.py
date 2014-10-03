from django.db import models


class User(models.Model):
    email = models.EmailField


class Device(models.Model):
    device_id = models.CharField
    name = models.CharField
    verification_token = models.CharField
    verified = models.BooleanField
    authentication_token = models.CharField
    authenticated = models.BooleanField
    user = models.ForeignKey(User)
