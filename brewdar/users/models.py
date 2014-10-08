from django.db import models
from django.core.exceptions import ValidationError
import string
import random


class User(models.Model):
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return self.email

    def is_valid(self):
        valid = False
        try:
            self.full_clean()
            valid = True
        except ValidationError as e:
            pass
        return valid


class Device(models.Model):
    device_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    verification_token = models.CharField(max_length=16)
    verified = models.BooleanField(default=False)
    authentication_token = models.CharField(max_length=16)
    authenticated = models.BooleanField(default=False)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.user.email + ", " + self.device_id

    def is_valid(self):
        valid = False
        try:
            self.full_clean()
            valid = True
        except ValidationError as e:
            pass
        return valid

    def verify(self, verification_token):
        if self.verification_token == verification_token:
            self.verified = True
            self.save()
            return True
        return False

    def generate_tokens(self):
        v_token = ''.join(random.sample(string.ascii_lowercase*16, 16))
        a_token = ''.join(random.sample(string.ascii_lowercase*16, 16))
        self.verification_token = v_token
        self.authentication_token = a_token
