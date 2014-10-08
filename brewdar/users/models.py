from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return self.email


class Device(models.Model):
    device_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    verification_token = models.CharField(max_length=16)
    verified = models.BooleanField()
    authentication_token = models.CharField(max_length=16)
    authenticated = models.BooleanField()
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.email + ", " + self.device_id

    def verify(self, verification_token):
        if self.verification_token == verification_token:
            self.verified = True
            self.save()
            return True
        return False

    def authenticate(self, authentication_token):
        if self.authentication_token == authentication_token:
            self.authenticated = True
            self.save()
            return True
        return False
